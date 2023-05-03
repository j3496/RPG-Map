# Made by Joel
# CS 30
#RPG game
#

import main


def Attack():
	# the attack menu
	print("Return to main menu")
	print("Return")
	print("Which attack do you want to use")
	print("Slash")
	print("Kick")
	print("Stomp")
	Attack1 = input("")
	if Attack1 == "Slash":
		print("Your attack did " + str(5) + " damage")
		menu()
	elif Attack1 == "Kick":
		print("Your attack did " + str(6) + " damage")
		menu()
	elif Attack1 == "Stomp":
		print("your attack did " + str(3) + " damage")
		menu()
	elif Attack1 == "Return":
		menu()
	else:
		print("Thats is not a valid attack")
		menu()


def Defend():
	print("Block \n Guard")
	Defend1 = input("")
	if Defend1 == "Block":
		print("You blocked the attack")
		menu()
	elif Defend1 == "Guard":
		print("You guard yourself")
		menu()
	else:
		print("that's not a valid defence")
		menu()


def Run():
	print("You escaped successfully")


def menu():
	# the main menu
	print("Attack")
	print("Defend")
	print("Run Away")
	print("Exit")
	menu1 = input("")
	if menu1 == "Attack":
		main.enemy()
	elif menu1 == "Defend":
		Defend()
	elif menu1 == "Run Away":
		Run()
	elif menu1 == "Exit":
		main.Exit()
	else:
		print("that's not a valid move")
