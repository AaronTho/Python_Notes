name = input("Type your name: ")
print("Welcome to this adventure,", name, ", I hope you survive the day.")

answer = input(
    "The dirt road you've been traveling has come to an end. You can go left into a dark mist or right into the light. Which way would you like to go? ").lower()

if answer == "left":
    went_left = input(
        "Eventually, you come to a river. You can walk around it or swim across. Type 'walk' to walk around or 'swim' to swim across: ").lower()

    if went_left == "swim":
        print("You swim into the river and are eaten by a small frog. You die to sound of elves laughing at you from the shore. Why on Earth did you choose the darkness?")

    elif went_left == 'walk':
        print("You walk for miles looking for away around the river. Eventually a small frog leaps from the river and consumes you whole. You hate dying this way. You hate the frog's breath. You hate the darkness.")
    else:
        print(
            "Not a valid option. You explode. A frog licks the pieces of you up and leaves.")

elif answer == "right":
    went_right = input(
        "You enter a forest of impossibly tall trees disapearing into the clouds. Type walk to enter the woods or climb to climb a tree: ").lower()

    if went_right == "walk":
        print()
    elif went_right == "climb":
        print()
else:
    print("Not a valid option. You explode.")
