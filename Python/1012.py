# -*- coding: utf-8 -*-

value = input().split(' ')


A = float(value[0])
B = float(value[1])
C = float(value[2])

pi = 3.14159

triangle = (A * C)/2 # The area of the rectangled triangle that has base A and height C
circle = pi * (C**2) # The area of the radius's circle C. (pi = 3.14159)
trapezium = (A+B) * (C/2) # The area of the trapezium which has A and B by base, and C by height.
square = B**2 # The area of ​​the square that has side B.
rectangle = A*B # The area of the rectangle that has sides A and B.



print("TRIANGULO: {:.3f}".format(triangle)) 
print("CIRCULO: {:.3f}".format(circle)) 
print("TRAPEZIO: {:.3f}".format(trapezium)) 
print("QUADRADO: {:.3f}".format(square)) 
print("RETANGULO: {:.3f}".format(rectangle))