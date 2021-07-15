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
        "You enter a forest of impossibly tall trees which disappear into the clouds. Type walk to enter the woods or climb to climb a tree: ").lower()

    if went_right == "walk":
        in_the_woods = input(
            "You walk through the forest. The air is heavy and lush and you hear singing in the wind. Type 'follow' to find source of the singing and 'onward' to continue deeper into the woods").lower()
        if in_the_woods == "follow":
            print("You follow the huanting sound of singing to a green sun-soaked meadow hidden deep in the trees. Frogs eat you to death and you die dead.It's so lame.")
        elif in_the_woods == "onward":
            print("You force yourself to ignore the pull of the forest singing and push through the forest until you find a 7-11 built into the trunk of one of the massive trees. You order a Slurpee and win the game.")
            quit()
        else:
            print("Not a valid option. You explode and die a fool.")

    elif went_right == "climb":
        print("You slowly climb the biggest tree you see, picking your way over the massive chunks of bark. At the top a bird looks at you and says, 'A frog is about to eat you, you never should have come up here.' She's right. You die.")
        quit()
else:
    print("Not a valid option. You explode.")
