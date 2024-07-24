number1 = [3, 5, 7, 2, 6]
number2 = [6, 3, 5, 0, 3]

number1.extend(number2)
new = set(number1)

print(list(new)[::-1])
# [7, 6, 5, 3, 2, 0]

