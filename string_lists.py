word = input("Pick a word: ").lower()
reverse = word[::-1]
if word == reverse:
    print(word + " spelt in reverse is " + reverse + ". This word is a palindrome.")
else:
    print(word + " spelt in reverse is " + reverse + ". This word is not a palindrome.")
