import datetime

name = input("What is your name? ")
age = int(input("How old are you? "))
number = int(input("Pick a number. "))
year = datetime.date.today().year
old = (100 - age) + year
print(number * (name + ", you will be 100 years old in the year " + str(old) + "!\n"))