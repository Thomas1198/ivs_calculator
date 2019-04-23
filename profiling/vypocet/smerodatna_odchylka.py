from main.modules.math import *

# @author xosols00
# vypocte smerodatnou odchylku z cisel vstupniho souboru

import sys

f=open('1000cisel.txt','r')
num = f.readline()
list=[]

list=num.split()
soucet=0

for num in list:
    soucet=add(soucet,int(num))

pocet=len(list)
print(pocet)
prumer=divide(soucet,pocet)

sum=0
for num in list:
    pom=subtract(int(num), prumer)
    sum=add(sum,power(pom, 2))

s=square(multiply(divide(1,subtract(pocet, 1)),sum))
print(s)