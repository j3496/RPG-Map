import main





def Enemy():
	"""fighting an enemy"""
	enemy_hp = 25
	while (enemy_hp >= 1):
		atk = input("Attacks: \n Slash \n Kick \n")
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
		print("You've killed the enemy\n You got a object")
		main.inventory.append("object")
		main.main()