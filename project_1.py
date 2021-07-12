import random
lower_letters_list = "abcdefghijklmnopqrstuvwxyz"
upper_letters_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numbers_list = "0123456789"

# The user inputs their requirements (eg. # of letters and numbers, lowercase, etc.) as well as preferences (including a specific word) and the program will generate a password for them.

password = ""

length = int(input("How many characters is your password? "))
lowercase = int(input("How many lowercase letters? "))
uppercase = int(input("How many uppercase letters? "))
numbers = int(input("How many numbers? "))
word = input("Any preferred words? ")

if word.lower() == "no":
    word = 0
elif word.lower() == "nope":
    word = 0
elif word.lower() == "nah":
    word = 0
elif word.lower() == "n":
    word = 0

if word != 0:
    while len(word)>length:
        print("Your word is too long.")
        word = input("Any preferred words? ")

if word == 0:
    total_characters = lowercase + uppercase + numbers
else:
    total_characters = lowercase + uppercase + numbers + len(word)
while total_characters > length:
    print("You have too many characters. Redo.")
    lowercase = int(input("How many lowercase letters? "))
    uppercase = int(input("How many uppercase letters? "))
    numbers = int(input("How many numbers? "))
    word = input("Any preferred words? ")
    if word == 0:
        total_characters = lowercase + uppercase + numbers
    else:
        total_characters = lowercase + uppercase + numbers + len(word)

# numbers, lowercase, uppercase, word

for i in range(numbers):
    random = randint(0, 9)
    password.append(numbers_list[random])

print(password)