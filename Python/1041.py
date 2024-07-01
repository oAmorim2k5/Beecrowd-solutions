X, Y = map(float, input().split(" "))


if X==0 and Y==0: #Origem
    print("Origem")
elif X != 0 and Y == 0: #Eixo X
    print("Eixo X")
elif X == 0 and Y != 0: #Eixo Y
    print("Eixo Y")
elif X>0 and Y>0: #Q1
    print("Q1")
elif X<0 and Y>0: #Q2
    print("Q2")
elif X<0 and Y<0: #Q3
    print("Q3")
elif X>0 and Y<0: #Q4
    print("Q4")