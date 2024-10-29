# take turns
import random

list = []
new_list = []

# make a function to ask who players are
def players():
    i = 0
    while i == 0:
        name = input("Who is playing: ")
        if name != "done":
            list.append(name)
        if name == "done":
            i += 1

# initiate players
players()

# randomize who goes first
first = random.randint(0, len(list)-1)
# create new list that starts with first and continues same order
new_list = list[first:] + list[:first]

# specify who is going first
print(f"{new_list[0]} is going first")

# make cycle of players
def cycle():
    j = 0
    while j == 0:
        for name in new_list:
            response = input(f"{name}, you are up! Type 'done' to continue, type 'end' to end: ")
            if response == "end":
                j += 1
                print("Game Over")
                return j
cycle()