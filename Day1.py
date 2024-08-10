import random


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



name = input('What is your name?\n')
print(f'Hello {name} !')


for index, chore in enumerate(household_chores):
    print(f'{index}. {chore}');

input('Pick a number of the chore to do today and I will tell your your today reward!\n')
print(f'Good choice, today reward is: {random.choice(rewards)}')


