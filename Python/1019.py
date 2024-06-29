entry = int(input())

hour = int(entry/3600)
minutes = int((entry%3600)/60)
seconds = int(entry%60)

print(f"{hour}:{minutes}:{seconds}")