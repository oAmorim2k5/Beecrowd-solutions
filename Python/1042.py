entry = input().split(" ")

numeric_list = list(map(int, entry))
list_sorted = sorted(numeric_list)

for i, elements in enumerate(list_sorted):
    print(elements)
print("")
for i, elements in enumerate(numeric_list):
    print(elements)

"""
x,y,z = list(map(int, input().split(" ")))
entry = [x, y, z]
entry.sort()

print(entry[0])
print(entry[1])
print(entry[2])
print("")
print(x)
print(y)
print(z)
"""