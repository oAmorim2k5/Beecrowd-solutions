a, b = map(int, input( ).split(' '))
        
if a < b:
    hours_game = b - a
else:
    hours_game = 24 - a + b
        
print(f"O JOGO DUROU {hours_game} HORA(S)")
