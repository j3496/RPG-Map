# Made by Joel
# CS 30
#RPG game
#

import Inventory
import enemy
import time

Enemy = 0
Spawn = 1
Escape = 2
Tile = 3


def Enemy():
	"""fighting an enemy"""
	enemy_hp = 25
	while (enemy_hp >= 1):
		atk = input(" Attacks: \n Slash \n Kick \n")
		if atk == "Slash":
			enemy_hp -= 5
			print(enemy_hp)
		elif atk == "yeet":
			enemy_hp -= 5000
		elif atk == "Kick":
			enemy_hp -= 6
			print(enemy_hp)
		else:
			print("Your attack failed")
	if enemy_hp <= 0:
		print("You've killed the enemy \nYou got a object")
		Inventory.inventory.append("object")
		main()


x = 1
y = 1
Loop = True

playermap = [
 "Tile", "Enemy", "Tile", "Enemy", "Escape", "Spawn", "Tile", "Tile", "Tile",
 "Enemy", "Enemy", "Tile", "Enemy", "Tile", "Enemy", "Enemy"
]

map = [[3, 0, 3, 0], [2, 1, 3, 3], [3, 0, 0, 3], [0, 3, 0, 0]]


def Exit():
	"""Ends the loop"""
	global Loop
	print("Good-bye")
	Loop = False


def Movement():
	"""lets you move around the map"""
	while True:
		movement = input("Where do you want to go? ")
		while True:
			global x
			global y
			if movement == "w":
				y += 1
				print("You moved forword 1 space ")
				break
			elif movement == "s":
				y -= 1
				print("You moved backwords 1 space ")
				break
			elif movement == "a":
				x -= 1
				print("You moved left 1 space ")
				break
			elif movement == "d":
				x += 1
				print("You moved right 1 space ")
				break
			else:
				print("You can't go that way ")
				Movement()
		a = room.x + x
		b = room.y + y
		room.userpos = map[a][b]
		# description of the rooms
		if room.userpos == 0:
			print("You've found an enemy")
			enemy.Enemy()
		elif room.userpos == 1:
			print("Spawn room")
		elif room.userpos == 2:
			print("You've successfully escaped")
			input("")
			time.sleep(31536000)
			print("Why is this code still running?")
			global Loop
			Loop = False


class Room(object):

	def __init__(self, x=4, y=4):
		self.userpos = map[x][y]
		self.x = x
		self.y = y


room = Room(0, 0)


def Map1():
	"""prints out the map to 'map.txt' """
	place = playermap
	with open("map.txt", "w") as file:
		file.write(f"{place}\n")


def main():
	"""lets you choose your inventory, print the map or to move around"""
	inp = input(
	 "To move type 'move' \n to access your inventory type 'inventory' \n you can quit the game at any time by pressing Ctrl + c \n To see the map type map "
	)
	if inp == "move":
		Movement()
	elif inp == "exit":
		try:
			Exit()
		except:
			print("\n")
			print("2")
		finally:
			print("\n")
			exit()
	elif inp == "map":
		"""prints the map to map.txt"""
		Map1()
		print("\nmap printed to 'map.txt'\n")
		main()
	elif inp == "inventory":
		print(Inventory.Inv())
		main()
	else:
		print("that's not a valid action")


try:
	main()
except:
	with open("error.txt", "w") as file:
		file.write("Error\n")
else:
	with open("error.txt", "w") as file:
		file.write("No errors\n")
