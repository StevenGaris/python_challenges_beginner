
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = []
max = int(input("Pick a number to find less than: "))
for number in numbers:
    if number < max:
        b.append(number)
print(b)
