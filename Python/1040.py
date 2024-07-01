n_um, n_dois, n_tres, n_quatro = map(float, input().split(" "))
media = ((n_um*2)+(n_dois*3)+(n_tres*4)+(n_quatro))/10

if media >= 7.0: #Aprovado
    print("Media: {:.1f}\nAluno aprovado.".format(media))
elif 7.0 > media >= 5.0: #Em exame
    print("Media: {:.1f}\nAluno em exame.".format(media))
    exame = float(input())
    print("Nota do exame: {:.1f}".format(exame))
    if exame >= 5.0:
        print("Aluno aprovado.\nMedia final: {:.1f}".format((media+exame)/2))
    else:
        print("Aluno reprovado.\nMedia final: {:.1f}".format((media+exame)/2))
elif media < 5.0: #Reprovado
    print("Media: {:.1f}\nAluno reprovado.".format(media))