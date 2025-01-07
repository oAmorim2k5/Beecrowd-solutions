entry = input( ).split(' ')

a = max(map(int, entry))
b = min(map(int, entry))

if(a%b != 0):
    print("Nao sao Multiplos")
else:
    print("Sao Multiplos")
