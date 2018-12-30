
divisor = int(input("Pick a number to get all of its divisors: "))
numbers = range(1, divisor+1)
result = []

for num in numbers:
    if divisor % num == 0:
        result.append(num)
print(result)