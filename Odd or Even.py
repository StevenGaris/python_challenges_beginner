
num = int(input("Pick a number: "))
check = int(input("Pick a number to divide by: "))
if num % 4 == 0:
    print(str(num) + " is a multiple of 4.")
elif num % 2 == 0:
    print(str(num) + " is an even number.")
else:
    print(str(num) + " is an odd number.")

if num % check == 0:
    print(str(check) + " divides evenly into " + str(num) + ".")
else:
    print(str(check) + " does not divide evenly into " + str(num)+ ".")