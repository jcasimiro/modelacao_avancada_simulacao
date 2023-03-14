import random

p = 1/2

output = []
dim_array = 10

for i in range(dim_array):
    n = random.random()
    if n > p:
        output.append(0)
    else:   
        output.append(1)

print(output)
print(str(sum(output)))

output2 = []
output2.append(output[0])
i = 1

while i < dim_array:
    if output[i] != output[i-1]:
        output2.append(1)
    else:
        output2.append(0)
    i += 1

print(output2)

#---------------------------
p01 = 1/2
p10 = 1/2

output3 = []

for i in range(dim_array):
    n = random.random()
    if output[i] == 0:
        if p01 > n:
            output3.append(1)
        else:
            output3.append(0)
    if output[i] == 1:
        if p10 > n:
            output3.append(0)
        else:
            output3.append(1)


p01=0
p00=0
p10=0
p11=0

for i in range(dim_array):
    n = random.random()
    if output[i] == 0 and output[i-1]==0:
        p00+=1
    elif output[i] == 0 and output[i-1]==1:
        p01+=1    

    elif output[i] == 1 and output[i-1]==1:
        p11+=1

    elif output[i] == 1 and output[i-1]==0:
        p10+=1    



a=p00+p01
b=p10+p11
p00=p00/(a)
p01=p01/(a)
p10=p10/(b)
p11=p11/(b)

print(p00,p01,p10,p11)

output4 = []

for i in range(dim_array):
    n = random.random()
    if output[i] == 0:
        if p01 > n:
            output4.append(1)
        else:
            output4.append(0)
    if output[i] == 1:
        if p10 > n:
            output4.append(0)
        else:
            output4.append(1)



print(output3)
print(output4)