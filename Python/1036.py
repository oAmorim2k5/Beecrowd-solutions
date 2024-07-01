import math

#Bhaskara = (-b±√(b²-4ac))/(2a)

A, B, C = map(float, input().split(" ")) #input

try:
    cont = (B**2)-4*(A*C)
    cont = math.sqrt(cont)
    contPos = (-B+cont)/(2*A)
    contNeg = (-B-cont)/(2*A)

    print("R1 = {:.5f}".format(contPos))
    print("R2 = {:.5f}".format(contNeg))
except:
    print("Impossivel calcular")