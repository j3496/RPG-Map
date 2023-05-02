
import Inventory

try:
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