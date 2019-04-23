from main.modules.math import *

# vypocte smerodatnou odchylku z cisel vstupniho souboru

import sys

#nacte cislice ze vstupniho souboru z argumentu
f = open("./"+sys.argv[1],'r')
num=f.readline()

list=[]

list=num.split(' ')
soucet=0

for num in list:
    soucet=soucet+int(num)

pocet=len(list)
print(pocet)
prumer=soucet/pocet

sum=0
for num in list:
    pom=int(num)-prumer
    sum=sum+power(pom, 2)

s=square(multiply(divide(1,pocet-1),sum))
print(s)