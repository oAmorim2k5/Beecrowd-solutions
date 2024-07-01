entry = float(input())
if 0 <= entry <= 25:
    print("Intervalo [0,25]")
elif 25.00001 <= entry <= 50:
    print("Intervalo (25,50]")
elif 50.00001 <= entry <= 75:
    print("Intervalo (50,75]")
elif 75.00001 <= entry <= 100:
    print("Intervalo (75,100]")
else:
    print("Fora de intervalo")