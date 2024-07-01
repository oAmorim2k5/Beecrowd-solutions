entry = float(input())
final = 0

if 0 <= entry <= 1000000.00:
    print("NOTAS:")
    print("{} nota(s) de R$ 100.00".format(int(entry/100)))
    entry %= 100
    print("{} nota(s) de R$ 50.00".format(int(entry/50)))
    entry %= 50
    print("{} nota(s) de R$ 20.00".format(int(entry/20)))
    entry %= 20
    print("{} nota(s) de R$ 10.00".format(int(entry/10)))
    entry %= 10
    print("{} nota(s) de R$ 5.00".format(int(entry/5)))
    entry %= 5
    print("{} nota(s) de R$ 2.00".format(int(entry/2)))
    entry %= 2

    print("MOEDAS:")
    print("{} moeda(s) de R$ 1.00".format(int(entry/1)))
    entry %= 1
    print("{} moeda(s) de R$ 0.50".format(int(entry/0.5)))
    entry %= 0.5
    print("{} moeda(s) de R$ 0.25".format(int(entry/0.25)))
    entry %= 0.25
    print("{} moeda(s) de R$ 0.10".format(int(entry/0.10)))
    entry %= 0.10
    print("{} moeda(s) de R$ 0.05".format(int(entry/0.05)))
    entry %= 0.05
    if entry >= 0.01:
        print("{} moeda(s) de R$ 0.01".format(int(entry/0.01)))
        entry %= 0.01
    elif entry >= 0.009:
        while entry >= 0.009:
          final += 1
          entry -= 0.009
        print(f"{final} moeda(s) de R$ 0.01")
    else:
        print(f"0 moeda(s) de R$ 0.01")
else:
 StopAsyncIteration