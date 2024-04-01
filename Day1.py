import random


rewards = [
    "Watching your favorite movie or TV show",
    "Taking a relaxing bath",
    "Going for a nature walk",
    "Listening to your favorite music playlist",
    "Reading a book or magazine",
    "Treating yourself to a spa day at home",
    "Buying yourself a small gift",
    "Spending time with a loved one",
    "Engaging in a hobby you enjoy",
    "Taking a nap or getting extra sleep"
]


household_chores = [
    "Vacuum the floors",
    "Wash the dishes",
    "Do the laundry",
    "Make the bed",
    "Clean the bathroom",
    "Take out the trash",
    "Wipe down kitchen counters",
    "Water the plants",
    "Sweep the porch",
    "Tidy up living room"
]


rewards = [
    "Watching your favorite movie or TV show",
    "Taking a relaxing bath",
    "Going for a nature walk",
    "Listening to your favorite music playlist",
    "Reading a book or magazine",
    "Treating yourself to a spa day at home",
    "Buying yourself a small gift",
    "Spending time with a loved one",
    "Engaging in a hobby you enjoy",
    "Taking a nap or getting extra sleep"
]
user = input("What is your name?\n")
print("Hello " + user + '!')
print('Pick a number of the chore to do today and I will tell your your reward!')

for index, chore in enumerate(household_chores):
    print(f"{index}. {chore}")

print('Write your choice here:')
number = input()

print(f'Perfect, you chose {number}. Your reward is: \'{rewards[int(number)]}\'')

