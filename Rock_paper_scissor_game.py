import random
#list of choices
choice = ["Rock", "Paper", "Scissor"]
#
length = len(choice) - 1
#
win = random.randint(0,length)
#game shooting choice
computer = input("Computer shoot: ")
human =input("Human shoot: ")
computer = int(computer)
human = int(human)
if human < 0 or human > 2:
    print("Invalid Human shoot, You lose")
else:
    winner = choice[win]
    if computer > human:
        print("{}, You lose".format(winner))
    elif human > computer:
        print("{}, You win".format(winner))
    elif computer == 0 and human == 2:
        print("{}, You lose".format(winner))
    elif computer == 2 and human == 0:
        print("{}, You win".format(winne))
    elif computer == human:
        print("{}, Draw".format(winner))
