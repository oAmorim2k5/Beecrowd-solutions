X, Y = map(int, input().split(" "))

cachorro_quente = 4.0 #id 1
x_salada = 4.5 #id 2
x_bacon = 5.0 #id 3
torrada_simples = 2.0 #id 4
refrigerante = 1.5 #id 5

match X:
    case 1:
        print("Total: R$ {:.2f}".format(cachorro_quente*Y))
    case 2:
        print("Total: R$ {:.2f}".format(x_salada*Y))
    case 3:
        print("Total: R$ {:.2f}".format(x_bacon*Y))
    case 4:
        print("Total: R$ {:.2f}".format(torrada_simples*Y))
    case 5:
        print("Total: R$ {:.2f}".format(refrigerante*Y))

"""
    case 5:
        print("Total: R$ {}".format(1.5*Y))
"""