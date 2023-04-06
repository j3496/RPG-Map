# Made by Joel
# CS 30
# 
# 

import menus
import enemy
Enemy = 0
Spawn = 1
Escape = 2
Tile = 3





x=1
y=1
Loop = True

map = [
	[3,0,3,0],
	[2,1,3,3],
	[3,0,0,3],
	[0,3,0,0]
]


def Exit():
	global Loop
	print("Good-bye")
	Loop = False


def Movement():
	"""lets you move around the map"""
	while True:
		movement = input("Where do you want to go?")
		while True:
			global x
			global y
			if movement == "w":
				x += 1
				print("You moved forword 1 space")
				break
			elif movement == "s":
				x -= 1
				print("You moved backwords 1 space")
				break
			elif movement == "a":
				y -= 1
				print("You moved left 1 space")
				break
			elif movement == "d":
				y += 1
				print("You moved right 1 space")
				break
			else:
				print("You can't go that way")
				Movement()
		a = room.x + x
		b = room.y + y
		room.userpos = map[a][b]
		# description of the rooms
		if room.userpos == 0:
			print("You've found an enemy")
			enemy.enemy()
		elif room.userpos == 1:
			print("Spawn room")
		elif room.userpos == 2:
			print("You've successfully escaped")
			global Loop
			Loop = False


class Room(object):
    def __init__(self, x=4, y=4):
        self.userpos = map[x][y]
        self.x = x
        self.y = y


room = Room(0, 0)


def main():
	"""lets you choose your inventory or to move around"""
	inp = input("To move type 'move' \n to access your inventory type 'inventory' \n you can quit the game at any time by pressing Ctrl + c ")
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


	elif inp == "inventory":
		print(enemy.inventory)
	else:
		print("that's not a valid action")


main()