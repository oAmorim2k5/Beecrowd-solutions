def triangle(a, b, c):
    if a >= b + c:
        print("NAO FORMA TRIANGULO")
        return
    if a**2 == b**2 + c**2:
        print("TRIANGULO RETANGULO")
    if a**2 > b**2 + c**2:
        print("TRIANGULO OBTUSANGULO")
    if a**2 < b**2 + c**2:
        print("TRIANGULO ACUTANGULO")
    if a == b == c:
        print("TRIANGULO EQUILATERO")
    if a == b and b != c or c == b and b != a:
        print("TRIANGULO ISOSCELES")

entry = input( ).split(' ')
a, b, c = sorted(map(float, entry), reverse=True)
triangle(a, b, c)
