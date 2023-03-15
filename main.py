Enemy = 0
Spawn = 1
Escape = 2
Tile = 3


map = [
	[3,1,3,1],
	[2,3,0,3],
	[3,0,0,3],
	[0,3,0,0]
]



def Movement():
	x = 1
	y = 1
	movement = input("Where do you want to go?")
	while True:
		if movement == "w":
			x += 1
			print("You moved forword 1 space")
		elif movement == "s":
			x -= 1
			print("You moved backwords 1 space")
		elif movement == "a":
			y -= 1
			print("You moved left 1 space")
		elif movement == "d":
			y += 1
			print("You moved right 1 space")
		else:
			print("You can't go that way")
			Movement()
	a = room.column + x
    b = room.row + y
    room.userpos = map[a][b]


def main():
	inp = input("")
	if inp == "move":
		Movement()
	elif inp == "inventory":
		inventory()
	else:
		print("that's not a valid action")
