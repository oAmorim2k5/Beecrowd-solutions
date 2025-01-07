def triangle(a, b, c):
    return ((a<b+c) and (b<a+c) and (c<a+b))
    
entry = input().split(' ')
a, b, c = map(float, entry)

if(triangle(a,b,c)):
    Perimetro = a+b+c
    print(f"Perimetro = {Perimetro:.1f}")
else:
    Area = ((a+b)*c)/2
    print(f"Area = {Area:.1f}")
