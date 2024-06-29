import math

one = str(input()).split(" ")
two = str(input()).split(" ")

x1 = float(one[0])
x2 = float(two[0])
y1 = float(one[1])
y2 = float(two[1])

distance = ((x2-x1)**2) + ((y2-y1)**2)
distance = math.sqrt(distance)


print("{:.4f}".format(distance))


