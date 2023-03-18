import csv
import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats

debug = False

#read csv file with inflation values
def read_inflation_rate(filename):
    list = []
    line=0
    with open(filename, newline='') as csvfile:
        inflation_reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        for row in inflation_reader:
            if (line > 0 ):
                list.append(float(row[1]))
            line += 1
    return list

#debug message function
def debug_message(label, value, spaces_after = 0):
    if debug:
        print(label + ": " + str(value))
        for i in range(spaces_after):
            print("")

# this is the function of parabolic kernel
def KdParabolicFunc(x0 , h , x):
    out = 0 
    if (abs((x-x0)/(h+0.0))<1):
        out = .75*(1-((x-x0)/(h+0.0))**2)/h
    return out

# developed by the work group
def calculate_density_estimation(inflation_list, median):
    x0 = stats.mean(inflation_list)
    output = []
    for i in range(len(inflation_list)):
        output.append(KdParabolicFunc(x0, median, inflation_list[i]))
    return output

# developed by the work group for analyze the calculation
def aux(xx, h, taxa):
    yy = np.zeros_like(xx)
    for i in range(xx.size):
        if (abs((taxa-xx[i])/(h+0.0))<1): 
            a = taxa-xx[i]
            b = a/h
            c = b**2
            d = 1-c
            e = d/h
            f = e*0.75
            yy[i] = .75*(1-((taxa-xx[i])/(h+0.0))**2)/h
        else:
            yy[i] = 0
    return yy

## the idea is now to produce averages from parabolic kernels with fixed h
# xarray keeps the positions of the center points
# h keeps the spread
# npts is the total number of points spread along the suppport of the average function.
def MeanKdParabolic(xarray , h , npts):
    x0 = np.min(xarray)
    xf = np.max(xarray)
    xx = np.linspace(x0-h , xf + h, endpoint=True , num=npts)
    yy = np.zeros_like(xx)
    for i in range(xarray.size):
        tmp = np.array(list(map(lambda x : 
                                .75*(1-((x-xarray[i])/(h+0.0))**2)/h if (abs((x-xarray[i])/(h+0.0))<1)
                                else  0 ,xx)))
        #tmp1 = aux(xx, h, xarray[i])
        yy += tmp
    return xx , yy/xarray.size

### Alternative implementation to get a function and not an array of images.
## the idea is now to produce averages from parabolic kernels with fixed h
# xarray keeps the positions of the center points
# h keeps the spread
# x is the point where we want to compute the function
def MeanKdParabolicFunc(xarray , h , x):   
    x0 = np.min(xarray)
    xf = np.max(xarray)  
    out = 0     
    for i in range(xarray.size):
        tmp = KdParabolicFunc(xarray[i] , h , x)
        out += tmp
    return out/xarray.size

def tax_simulation(inflation_list_array, yy01, xx01, hh01):
    # we use the acception-rejection method to generate the random deviates
    # this variable keeps the number of simulations produced to compute the relative efficiency
    generated = 0

    # this variable counts how many deviates where already generated
    count = 0 
    # the number of random values that we need
    ndeviates = 1000

    # we will generate random uniforms in the interval [0,ytecto]
    ytecto = np.max(yy01)

    # the interval in which we generate random deviates
    xmin = np.min(xx01)
    xmax = np.max(xx01)

    # where everythong is stored
    rlista = []

    while(count < ndeviates):
        generated += 1 
        
        tx = random.uniform(xmin,xmax)
        ty = random.uniform(0,ytecto)
        
        if (ty < MeanKdParabolicFunc(inflation_list_array,hh01,tx)):
            rlista.append(tx)
            count += 1
            
    ratio = (ndeviates + 0.)/generated
    mean = stats.mean(rlista)

    #print("The acceptance ratio was %f" %ratio)
    #print("Mean value: %f" %mean)

    #plt.hist(rlista , density = True , bins = 50 , rwidth = .8 , color = (.3,.4,.6,.3))
    #plt.plot(xx01,yy01,linewidth=2,color=(0. , 0 , 0 , .8))
    #plt.show()

    return mean

def credit_simulation(Tx):
    if len(Tx) != 30:
        return None

    valor_emprestimo = 100000  # €
    prazo = 30  # anos
    spread = 0.02  # 2%
    divida =np.zeros(prazo)
    juro_total=np.zeros(prazo)
    prestacao_anual=np.zeros(prazo)
    juro_capital_em_divida =np.zeros(prazo)
    amortizacao=np.zeros(prazo)
    anos_em_falta=np.zeros(prazo)
    coltab = []    

    # ano zero dp emprestimo
    divida[0]=valor_emprestimo
    anos_em_falta[0]=prazo
    juro_total[0]=Tx[0]/100+spread
    prestacao_anual[0]=divida[0]*((1-(1/(1+juro_total[0])))/((1/(1+juro_total[0]))-(1/(1+juro_total[0]))**(anos_em_falta[0]+1)))
    juro_capital_em_divida[0]=juro_total[0]*divida[0]
    amortizacao[0]=prestacao_anual[0]-juro_capital_em_divida[0]

    coltab.append([Tx[0]/100, divida[0], juro_total[0],prestacao_anual[0],juro_capital_em_divida[0],amortizacao[0]])

    for i in range(1,prazo):
        anos_em_falta[i]=anos_em_falta[i-1]-1
        divida[i]=divida[i-1]-amortizacao[i-1]
        juro_total[i]=Tx[i]/100+spread
        prestacao_anual[i]=divida[i]*((1-(1/(1+juro_total[i])))/((1/(1+juro_total[i]))-(1/(1+juro_total[i]))**(anos_em_falta[i]+1)))
        juro_capital_em_divida[i]=juro_total[i]*divida[i]
        amortizacao[i]=prestacao_anual[i]-juro_capital_em_divida[i]
        coltab.append([Tx[i]/100, divida[i], juro_total[i],prestacao_anual[i],juro_capital_em_divida[i],amortizacao[i]])
        
    # Criação do DataFrame - tabela
    colunas = ['Juro Simulado', 'Dívida', 'Juro Total', 'Prestação Anual', 'Juro Capital em Divida','Amortização']
    tabela = pd.DataFrame(coltab, columns=colunas)

    print(tabela)

def main():
    #read the file
    inflation_list = read_inflation_rate("FPCPITOTLZGUSA.csv")
    out = calculate_density_estimation(inflation_list, 10)

    #plt.fill(inflation_list, out, color=(.3,.3,.3,.3))
    #plt.plot(inflation_list, out, linewidth=2,color='k')
    #plt.grid(True)
    #plt.show()

    inflation_list_array = np.array(inflation_list)

    #1000
    npts01 = 1000
    #2
    hh01 = 2
    xx01 , yy01 = MeanKdParabolic(inflation_list_array , hh01 , npts01)

    # this must produce exactly the same result as yy01
    yy02 = np.array(list(map(lambda x : MeanKdParabolicFunc(inflation_list_array,hh01,x) , xx01)))

    #plt.fill(xx01,yy01,color=(.3,.3,.3,.3))
    #plt.plot(xx01 , yy01,linewidth=2,color='k')
    #plt.grid(True)
    #plt.show()

    taxas_simulacao = []
    for i in range(0, 30):
        taxas_simulacao.append(tax_simulation(inflation_list_array, yy01, xx01, hh01))

    credit_simulation(taxas_simulacao)

if __name__ == "__main__":
    main()