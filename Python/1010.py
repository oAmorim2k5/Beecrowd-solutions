# -*- coding: utf-8 -*-

enterOne = input()
enterTwo = input()

#inputs
val = str(enterOne).split(" ")
valTwo = str(enterTwo).split(" ")

# 0 Code, 1 units, 2 price
nOne = int(val[0])
nTwo = float(val[1])
nTree = float(val[2])

mOne = int(valTwo[0])
mTwo = float(valTwo[1])
mTree = float(valTwo[2])

price = (nTwo * nTree) + (mTwo * mTree)

print("VALOR A PAGAR: R$ {:.2f}".format(price))