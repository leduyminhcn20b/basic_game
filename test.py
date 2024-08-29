from random import randint

print("You choose (Dam, La, Keo ) :")
player = input()

computer = randint(0,2)
if(computer == 0):
    computer = "Dam"
elif(computer == 1):
    computer = "La"
elif(computer == 2):
    computer = "Keo"

print(str("Computer choose : ") + computer)

if player == computer:
    print("Draw")
else:
    if player == "Keo":
        if computer == "Dam":
            print("Lose : Dam > Keo")
        if computer == "La":
            print("Win : Keo > La")
    elif player == "Dam":
        if computer == "Keo":
            print("Win : Dam > Keo")
        if computer == "La":
            print("Lose : La > Dam")
    elif player == "La":
        if computer == "Keo":
            print("Lose : Keo > La")
        if computer == "Dam":
            print("Win : La > Dam")
    else:
        print("INPUT ERROR !!")
