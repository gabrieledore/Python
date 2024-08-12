import random

letters = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z'
]

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
symbols = [
  '!', '@', '#', '$', '%', '^', '&', '*', '(', ')',
  '-', '_', '=', '+', '[', ']', '{', '}', '\\', '|',
  ';', ':', "'", '"', ',', '.', '/', '<', '>', '?',
  '~', '`'
];

password = ''
userLetters = int(input("How many letters would you want in your password?\n"))
userNumbers = int(input("How many numbers?\n"))
userSymbols = int(input("How many symbols?\n"))

for char in range(0, userNumbers):
    password += (random.choice(letters))
for number in range(0, userNumbers):
    password += str(random.choice(numbers))
for symbol in range(0, userSymbols):
    password += (random.choice(symbols))


final_word = "".join(random.sample(password, len(password)))
print(final_word)