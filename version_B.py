from random import randint

t = ["sasso", "carta", "forbice"]

computer = t[randint(0, 2)]

player = False

while player == False:

    player = input("sasso carta o forbice?")
    if player == computer:
        print("Pareggio!")
    elif player == "sasso":
        if computer == "carta":
            print("hai perso!", computer, "copre", player)
        else:
            print("hai vinto!", player, "rompe", computer)
    elif player == "carta":
        if computer == "forbice":
            print("hai perso!", computer, "taglia", player)
        else:
            print("hai vinto!", player, "copre", computer)
    elif player == "forbice":
        if computer == "sasso":
            print("hai perso...", computer, "rompe", player)
        else:
            print("hai vinto!", player, "taglia", computer)
    else:
        print(" Non è un input valido. Controlla la tua ortografia!")

    player = False
    computer = t[randint(0,2)
	
	
