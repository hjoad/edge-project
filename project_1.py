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

while len(word)>length:
    print("Your word is too long.")
    word = input("Any preferred words? ")

total_characters = lowercase + uppercase + numbers + len(word)
while total_characters > length:
    print("You have too many characters. Redo.")
    lowercase = int(input("How many lowercase letters? "))
    uppercase = int(input("How many uppercase letters? "))
    numbers = int(input("How many numbers? "))
    word = input("Any preferred words? ")
    total_characters = lowercase + uppercase + numbers + len(word)