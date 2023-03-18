import numpy as np
import matplotlib.pyplot as plt
import random
import statistics

plt.rcParams['figure.figsize']=(12,8)

# this version generate an array of points of the parabolic kernel
def KdParabolic(x0 , h , npts):
    
    xx = np.linspace(x0-h , x0+h , num=npts , endpoint=True)
    yy = np.array(list(map(lambda x: .75*(1-((x-x0)/(h+0.0))**2)/h,xx)))
    
    return xx , yy

# this is the function of parabolic kernel
def KdParabolicFunc(x0 , h , x):
    
    out = 0 
    
    if (abs((x-x0)/(h+0.0))<1):
        out = .75*(1-((x-x0)/(h+0.0))**2)/h
        
    return out

hh10 = 3 
cc10 = 5
npts10 = 200

xx10 , yy10 = KdParabolic(cc10 , hh10 , npts10)

# now we apply the function to the xx10 array. the result must be exactly equal to yy10
yy11 = np.array(list(map(lambda x : KdParabolicFunc(cc10 , hh10, x) , xx10)))

#plt.fill(xx10,yy10,color=(.3,.3,.3,.3))
#plt.plot(xx10,yy10,linewidth=2,color='k')
#plt.grid(True)
#plt.show()

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

xinit = 5
xfinit = 10

teste01 = xinit + (xfinit - xinit) * np.random.uniform(size=20)
npts01 = 1000
hh01 = 2

xx01 , yy01 = MeanKdParabolic(teste01 , hh01 , npts01)

# this must produce exactly the same result as yy01
yy02 = np.array(list(map(lambda x : MeanKdParabolicFunc(teste01,hh01,x) , xx01)))

#plt.fill(xx01,yy01,color=(.3,.3,.3,.3))
#plt.plot(xx01 , yy01,linewidth=2,color='k')
#plt.grid(True)
#plt.show()

# we use the acception-rejection method to generate the random deviates

# this variable keeps the number of simulations produced to compute the relative efficiency
generated = 0

# this variable counts how many deviates where already generated
count = 0 
# the number of random values that we need
ndeviates = 50000

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
    
    if (ty < MeanKdParabolicFunc(teste01,hh01,tx)):
        rlista.append(tx)
        count += 1
        
ratio = (ndeviates + 0.)/generated

print("The acceptance ratio was %f" %ratio)

plt.hist(rlista , density = True , bins = 50 , rwidth = .8 , color = (.3,.4,.6,.3))
plt.plot(xx01,yy01,linewidth=2,color=(0. , 0 , 0 , .8))
plt.show()