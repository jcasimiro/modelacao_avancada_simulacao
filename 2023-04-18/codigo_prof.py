import random
import numpy as np

def unitgen():
    out = 0
    if random.random() < .5:
        out = 1
    
    return out

distconjunta = np.array([[0.6,0.1],[0.15,.15]])
margx = np.sum(distconjunta,axis=1)
margy = np.sum(distconjunta,axis=0)

npts = 500
xrand = np.zeros(npts).astype(int)
yrand = np.zeros(npts).astype(int)

for i in range(npts):
    newx = unitgen()
    alphax = random.uniform(0,1)
    if alphax < distconjunta[newx,yrand[i]]/margy[yrand[i]]:
        xrand[i] = newx

    newy = unitgen()
    alphay = random.uniform(0,1)
    if alphay < distconjunta[xrand[i],newy]/margx[xrand[i]]:
        yrand[i] = newy


for i in range(npts):
    print((xrand[i],yrand[i]))

