values = input().split(' ')
a, b, c = values

ab = (int(a)+int(b) + abs(int(a)-int(b)))/2 # 1º
result = (int(c)+int(ab) +abs(int(c) - ab))/2 # 2º

result = int(result)
print(f"{result} eh o maior")

"""
1º  The sum of a and b ensures the final result is at least the larger of the two.
    abs(int(a) - int(b)) calculates the absolute difference between a and b.
    Dividing by 2 serves as a "rounding" mechanism to consider the absolute difference.

2º  Calculates the largest between c and the previous value (ab). The logic resembles line 3.

"""
