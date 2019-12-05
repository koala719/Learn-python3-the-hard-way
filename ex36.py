from sys import exit


def dead(why):
    print(why, "Good job!")
    exit(0)

def start():
    print("You are in a dark room.")
    print("There is a door to your right and left.")
    print("Is lidafan love koala?")

    choice = input("> ")

    if choice == "yes":
        print("You win!")
    else:
        dead("You lost everything.")

start()
