##Carro uses 12km/L
##How many time in travel
##Speed car Km/h

## time*km/12

time = int(input())
kmHour = int(input())

fuel = (time*kmHour)/12
print("{:.3f}".format(fuel))