import random

output = []
#configuracao inicial
output.append(0)
p00 = 1/3
p01 = 1/3
p02 = 1/3

p10 = 1/3
p11 = 1/3
p12 = 1/3

p20 = 1/3
p21 = 1/3
p22 = 1/3

n_elements = 100

for i in range(n_elements):
    n = random.random()
    if output[i]==0:
        if n > p00:
            output.append(0)
        else:   
            n = random.random()-p00
            if n > p01:
                output.append(1)
            else:
                output.append(2)
                
    if output[i]==1:
        if n > p11:
            output.append(1)
        else:   
            n = random.random()-p11
            if n > p10:
                output.append(0)
            else:
                output.append(2)
    if output[i]==2:
        if n > p22:
            output.append(2)
        else:   
            n = random.random()-p22
            if n > p20:
                output.append(0)
            else:
                output.append(1)

print(output)