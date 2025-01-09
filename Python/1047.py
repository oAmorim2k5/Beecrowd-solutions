a, b, c, d = map(int, input( ).split(' '))

if a < c:
    game_hours = c - a
elif c < a:
    game_hours = 24 - a + c
else:
    game_hours = 24

if b <= d:
    game_minutes = d - b
else:
    game_minutes = 60 - b + d
    game_hours -= 1
    
if game_hours == 24 and game_minutes != 0:
    game_hours = 0
    
print(f"O JOGO DUROU {game_hours} HORA(S) E {game_minutes} MINUTO(S)")
