i = int(input())

print(i)
print("{} nota(s) de R$ 100,00".format(int(i/100)))
rest = (i%100)
print("{} nota(s) de R$ 50,00".format(int(rest/50)))
rest = (rest%50)
print("{} nota(s) de R$ 20,00".format(int(rest/20)))
rest = (rest%20)
print("{} nota(s) de R$ 10,00".format(int(rest/10)))
rest = (rest%10)
print("{} nota(s) de R$ 5,00".format(int(rest/5)))
rest = (rest%5)
print("{} nota(s) de R$ 2,00".format(int(rest/2)))
rest = (rest%2)
print("{} nota(s) de R$ 1,00".format(int(rest/1)))