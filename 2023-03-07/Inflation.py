import csv

def k(x):
    if x <= -2 or x >= 2:
        return 0
    if x >= -2 and x <= 0:
        return 0.5+0.25*x;
    if x > 0 and x <= 2:
        return 0.5-0.25*x;

list = []
i = 0

with open('2023-03-07/FPCPITOTLZGUSA.csv', newline='') as csvfile:
    inflation_reader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    for row in inflation_reader:
        if (i > 0 ):
            list.append(float(row[0].split(',')[1]))
        i = i + 1

n = len(list)
x = 1
total = 0

for e in list:
    total = total + k(x - e)
    print(total)

total = total / n