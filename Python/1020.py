entry = int(input())

years = print("{} ano(s)".format(int(entry/365)))
months = print("{} mes(es)".format(int((entry%365)/30)))
days = print("{} dia(s)".format(int((entry%365)%30)))