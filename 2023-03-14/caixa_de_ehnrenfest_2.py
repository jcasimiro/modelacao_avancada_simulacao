import random

output = []
#configuracao inicial
output.append(0)
p00 = 0.2
p01 = 0.3
p02 = 0.5

p10 = 0.1
p11 = 0.3
p12 = 0.6

p20 = 0.2
p21 = 0.3
p22 = 0.5

n_elements = 100

for i in range(n_elements):
    n = random.random()
    if output[i]==0:
        if n > p00:
            output.append(0)
        else:   
            n = random.uniform(0,(1-p00))
            if n > p01:
                output.append(1)
            else:
                output.append(2)
    n = random.random()            
    if output[i]==1:
        if n > p11:
            output.append(1)
        else:   
            n = random.uniform(0,(1-p11))
            if n > p10:
                output.append(0)
            else:
                output.append(2)
    n = random.random()
    if output[i]==2:
        if n > p22:
            output.append(2)
        else:   
            n = random.uniform(0,(1-p22))
            if n > p20:
                output.append(0)
            else:
                output.append(1)

print(output)