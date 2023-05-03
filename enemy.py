# Made by Joel
# CS 30
#RPG game
#

import Inventory


def Enemy():
	"""fighting an enemy"""
	try:
		enemy_hp = 25
		while (enemy_hp >= 1):
			atk = input(" Attacks: \n Slash \n Kick \n Stomp \n")
			if atk == "Slash":
				enemy_hp -= 5
				print("Your attack did 5 damage")
				print(enemy_hp)
				enemy_attack.Slash
			elif atk == "yeet":
				enemy_hp -= 5000
			elif atk == "Kick":
				enemy_hp -= 6
				print("Your attack did 6 damage")
				print(enemy_hp)
			elif atk == "Stomp":
				enemy_hp -= 3
				print("Your attack did 3 damage")
				print(enemy_hp)
			else:
				print("Your attack failed")
		if enemy_hp <= 0:
			print("You've killed the enemy \nYou got a object")
			input("press enter to continue")
			Inventory.pick()
	except:
		print("There was an error running the 'enemy' code")
	else:
		print("\n \n")
	finally:
		with open("enemys.txt", "w") as file:
			file.write("The enemy file worked\n")
		with open("enemys.txt", "a") as file:
			file.write(f"{Inventory.Inv()}\n")


class enemy_attack():
	"""Enemy attacking the player"""
	player_hp = 25
	while (player_hp >= 1):

		def Slash():
			global player_hp
			player_hp -= 5
			print("You got Slashed for 5 damage")
			print(player_hp)

		def Kick():
			global player_hp
			player_hp -= 6
			print("You got Kicked for 6 damage")
			print(player_hp)

		def Stomp():
			global player_hp
			player_hp -= 3
			print("You got Stomped for 3 damage")
			print(player_hp)

	if player_hp <= 0:
		print("You Died")
