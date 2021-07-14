import random
lower_letters_list = "abcdefghijklmnopqrstuvwxyz"
upper_letters_list = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

# The user inputs their requirements (eg. # of letters and numbers, lowercase, etc.) as well as preferences (including a specific word) and the program will generate a password for them.

password = ""

length = int(input("How many characters is your password? "))
min_length = int(input("Minimum password length? "))
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
while total_characters > length or total_characters < min_length:
    if total_characters > length:
        print("You have too many characters. Redo.")
    elif total_characters < min_length:
        print("You have too few characters. Redo.")
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
    if word == 0:
        total_characters = lowercase + uppercase + numbers
    else:
        total_characters = lowercase + uppercase + numbers + len(word)

# numbers, lowercase, uppercase, word
# # check if we can randomize order

for i in range(numbers):
    n = random.randint(0, 9)
    password = password + str(n)

for i in range(lowercase):
    n = random.choice(lower_letters_list)
    password = password + str(n)

for i in range(uppercase):
    n = random.choice(upper_letters_list)
    password = password + str(n)

if word != 0:
    password = password + word

print(password)

file = open("password.txt", "w+")
file.write(password)
file.close()