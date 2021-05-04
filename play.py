def play():
	from tqdm import tqdm
	import time
	start=input("Are you ready to play? If you wanna start, enter 's'. If not, enter 'a': ")
	if start=='s':
		print("--------------------------------INTRO---------------------------------\n[TV turns on]\nMayor Fredrickson: 'As the mayor, I hereby declare the Tunisian Archeological Exhibit...' \n[The camera zooms out, the TV is now visible in Henry's house]\n 'Open!' \n[Henry realizes it's worth, as his eyes turns into dollar signs]\nMayor Fredrickson: 'Yes. Thank you. Myes.'\n[Henry grabs his keys]")
		for i in tqdm (range (101),
				desc="Loading…",
				ascii=False, ncols=75):
	      	    time.sleep(0.01)
	#stage 1
		stage1=input("-------------------------------STAGE 1--------------------------------\nHenry is now near the wall of the museum. \nHe has two options: Sneak in and Bust in. \nWhat should he do? \nIf you want him to Sneak in, enter '1' \nand if you want him to bust in, enter '2': ")
		for i in tqdm (range (101),
				desc="Loading…",
				ascii=False, ncols=75):
	      	    time.sleep(0.01)
	
		if stage1=='1':
			#stage2
			stage2=input("-------------------------------STAGE 2--------------------------------\nNow Henry has two options. \nHe can go forward towards the wall, or up towards the roof. \nIf you want him to go forward, enter '1' and if up, enter '2': ")
			if stage2=='1':
				for i in tqdm (range (101),
				desc="Loading…",
				ascii=False, ncols=75):
					time.sleep(0.01)
				print("You have chosen to go forward!")
				stage3=input("-------------------------------STAGE 3--------------------------------\nNow, what would you like to use? Shrink Ray, Picaxe, or Liquidificator. \nIf you want to use Shrink Ray, enter '1' \nIf you want to use Picaxe , enter '2' \n and if ya wanna use Liquidificator, enter '3'.")
				if stage3=='1':
					print("FAIL\nYou shrunk yourself and an earthworm made you his supper. \nTo retry, rerun the whole program.")
				elif stage3=='3':
					print("FAIL\nYou used the liquidificator and became water getting soaked by the soil. \nTo retry, rerun the whole program.")
				elif stage3=='2':
					for i in tqdm (range (101),
							desc="Loading…",
							ascii=False, ncols=75):
	          				time.sleep(0.01)
					print("While you were breaking the wall with a picaxe, a minecraft creeper came behind you and blew up. The wall has been broken successfully.")
					for i in tqdm (range (101),
							desc="Loading…",
							ascii=False, ncols=75):
									time.sleep(0.01)
					stage4=input("-------------------------------STAGE 4--------------------------------\nThere are two guards in front of you talking. \nRight now they can't see you, but you must get rid of them or else they'll catch you.\nTo use the bombshell in front of you, enter '1' \nif you wanna use the rifle on the wall of the museum, enter '2' \nand if you wanna use the toy plane model, enter '3': ")
					for i in tqdm (range (101),
							desc="Loading…",
							ascii=False, ncols=75):
									time.sleep(0.01)
					if stage4=='1':
						print("FAIL\nYou threw the bombshell but it didn't blow up because it was fake. \nTo retry, rerun the whole program.")
					elif stage4=='2':
						print("FAIL\nYou picked up the gun, but those cops have better reflexes than you imagined. \nTo retry, rerun the whole program.")
					elif stage4=='3':
						print("You threw a plane on one of the guards and knocked him out. \nThe other guard got scared and ran for his life.")
						stage5=input("-------------------------------STAGE 5--------------------------------\nThe guard that was running knocked his head with a pillar. \nYou run all the way to that pillar. \nThere are two doors which lead to two rooms: The Retro Room and the Grand Exhibit which has the Diamond. \nBut unluckily, there is a guard protecting the rooms, standing next to the open door of the Grand Exhibit. \nBut the good news is, he seems to be asleep.\nWhere will you go now? \nIf you wanna go into the retro room, enter '1' \nor if ya wanna go into the Grand Exhibit, enter '2': ")
						if stage5=='2':
							print("FAIL\nYou just Naruto ran towards the room, but the guard was a light sleeper. \nTo retry, rerun the whole program.")
						elif stage5=='1':
							for i in tqdm (range (101),
							desc="Loading…",
							ascii=False, ncols=75):
									time.sleep(0.01)
							print("You Naruto ran extremely fast into the Retro Room, and luckily, the guard didn't notice you.")
							stage6=input("-------------------------------STAGE 6--------------------------------\nNow from the Retro Room, you enter open a door that leads to the Grand Tunisian Exhibit. \nTo stay unnoticed, you close the door. \nYou have four options: \nto use the Goodball(Green Pokeball), enter '1', \nto use the crowbar, enter '2', \nto use the alien, enter '3', and \nto use the giant Mario Mushroom, enter '4': ")
							if stage6=='1':
								print("FAIL\nHenry challenges guards to a fight.\nGuards send out Joe.\nHenry sends out MissingNo.\nGame starts glitching.\n\n01000110 01000101 01000001 01010010 00100000 01001101 01001001 01010011 01010011 01001001 01001110 01000111 01001110 01001111 \nTo retry, rerun the whole program.")
							elif stage6=='2':
								print("FAIL\nHenry touches the crowbar and looks up. \nA ton of head crabs fall on his head. \nTo retry, rerun the whole program.")
							elif stage6=='3':
								print("FAIL\nThe aliens don't take orders. \nTo retry, rerun the whole program.")
							elif stage6=='4':
								print("You used the giant mushroom. \n Now you are big, just like when Mario eats his mushrooms.")
								for i in tqdm (range (101),
								desc="Loading…",
								ascii=False, ncols=75):
										time.sleep(0.01)
								print("-------------------------------STAGE 7--------------------------------\n You broke the wall of the room. \nThe guards have noticed you, and now they are firing bullets at you, but the bullets seem to have no effect on you! \n While you are stomping your way through, a dinosaur egg cracked, and a baby pterodactyl was released. \nThe guards have called for backup, and one of them has even brought  canon. \nThe gaurds are attacking you continuously, but you have seem to become immune. \nThe baby dinosaur eats up one of the guards. \nYou continue marching and finally reach the diamond. \nNow the diamond is yours!")
								for i in tqdm (range (101),
								desc="Loading…",
								ascii=False, ncols=75):
										time.sleep(0.1)
								print("Oh no! A giant cannonball knocked you down. The diamond is out of your hands! XC \n")
								print("[Meanwhile, somewhere in the southwest...] \n[At the CCC{Center of Chaos Containment}...] \n[Man1: Uh sir, you might wanna see this.]\n[Sir arrives]\n[Man1: I am getting chaos readings at 10.6...it's coming from the museum.]\n[Sir: My god, it's over 9!]\n[Man1:Yeah]\n[Sir: I am leaving this decision upto you Corporal. Just hit one of those buttons to deal with this...pressing situation.]\n{looks elsewhere}\n[Sir: Who's watching TV? Get back to work!]")
								stage7=input("\nSo Corporal, this is upto you!\nYou must help Henry! \nTo make a nuclear explosion, enter '1', \nTo contact the satellite, enter '2', \nTo spawn a robot, enter '3', \n To give him a calculator and a division sum, enter '4': ")
								if stage7=='1':
									print("FAIL\nThe nuke blew everything up. \nTo retry, rerun the whole program.")
								elif stage7=='2':
									print("FAIL\nThe satellite destroyed the museum. \nTo retry, rerun the whole program.")
								elif stage7=='4':
									print("FAIL\nThe denominator was zero, so the calculator messed up. \nTo retry, rerun the whole program.")
								elif stage7=='3':
									print("-------------------------------STAGE 8--------------------------------\nOMG! A giant robot is spawned at the museum, and it is destroying everything. \n Oh no, you {Henry} have become small again! \n Now you are running away, because you realised that your life is more important than the diamond. \nHow Sad......")
									for i in tqdm (range (101),
									desc="Loading…",
									ascii=False, ncols=75):
											time.sleep(0.1)
									print("Wait...The Giant Diamond somehow landed on the grass next to you!")
									print("-------------------------------YOU WON--------------------------------\nRANK:\nJUST PLAIN EPIC\n")

			if stage2=='2':
				for i in tqdm (range (101),
							desc="Loading…",
							ascii=False, ncols=75):
									time.sleep(0.01)
				stage3=input("-------------------------------STAGE 3--------------------------------\nNow Henry has 3 options. \nEither he can use Jumble Hoppers, an Anti-Gravity Cap and the Teleporter. \nIf ya wanna use Jubble Hoppers, enter '1' \nIf ya wanna use Anti-Gravity Cap, enter '2' \nIf ya wanna use the Teleporter, enter 3:")
				if stage3=='1':
					print("FAIL\nYou jumped really high with those Jubble Hoppers, but you couldn't reach the roof. You fell down and flipped into the pond nearby. \nTo retry, rerun the whole program.")
				elif stage3=='2':
					print("FAIL\nYou just kept on flying up in the air. Although you've always wanted to o to space, I don't think you wanted to go like this. \nTo retry, rerun the whole program.")
				elif stage3=='3':
					for i in tqdm (range (101),
							desc="Loading…",
							ascii=False, ncols=75):
									time.sleep(0.01)
					stage4=input("-------------------------------STAGE 4--------------------------------\nYou succesfully teleported to the roof of the Museum. \nThere is a door from where you can go in, but it is protected by a guard. \nYou are hiding behind a big box where the guard can't see you. \nYou can do 4 things: \n- To use a penny, enter '1' \n- To use a Tranquilizer Gun, enter '2' \n- To give him a Falcon Punch, enter '3' \n-To use the invisibility pill, enter '4'. \nSo whatcha gonna do?")
					if stage4=='2':
						print("FAIL\nYou shot him and he fell asleep blocking the door. \nTo retry, rerun the whole program.")
					elif stage4=='3':
						print("FAIL\nYou tried to give him a falcon punch, but you were too slow so he shot you. \nTo retry, rerun the whole program.")
					elif stage4=='4':
						print("FAIL\nYou became invisible but we lost track of your location. \nTo retry, rerun the whole program.")
					elif stage4=='1':
						for i in tqdm (range (101),
							desc="Loading…",
							ascii=False, ncols=75):
									time.sleep(0.01)
						stage5=input("-------------------------------STAGE 5--------------------------------\nThe guard got distracted by your coin and so while he went to pick it up, you ran really fast into the museum. \nYou are on a platform, right above the giand diamond in the grand exhibit. \nYou have 3 options: \nIf you wanna drop down, enter '1', \nIf ya wanna use the wire, enter '2' \nOr if u wanna use the wormhole rifle, enter '3': ")
						for i in tqdm (range (101),
							desc="Loading…",
							ascii=False, ncols=75):
									time.sleep(0.01)
						if stage5=='1':
							print("FAIL\nYou just fell and fractured yourself severely. \nTo retry, rerun the whole program.")
						elif stage5=='3':
							print("FAIL\nYou spawned a wormhole through which the diamond fell and you spawned one right on top of it, so now you and the diamond are stuck inside the space-time continuum. Great technology, wrong use.\nTo retry, rerun the whole program.")
						elif stage5=='2':
							stage6=input("-------------------------------STAGE 6--------------------------------\nYou went down using the rope, and no one saw you. How Lucky! \nThe Diamond is in a glass cube. \nTo take it out, you may use: \n- a laser cutter {1} \n- a hammer {2}: ")
							for i in tqdm (range (101),
							desc="Loading…",
							ascii=False, ncols=75):
									time.sleep(0.01)
							if stage6=='1':
								print("FAIL\nYou just setup the laser cutter backward so it cut you instead of the glass. \nTo retry, rerun the whole program.")
							elif stage6=='2':
								stage7=input("-------------------------------STAGE 7--------------------------------\nThe hammer easily broke the glass cube and you took the diamond out.\nIt is very heavy. You run to the next room where 2 guards are chatting. \nYou have 3 options: \nEither you can use a cannon {1}, a slice of cheese {2}, or a wooden plank {3} \nWhat do you want to do? ")
								for i in tqdm (range (101),
								desc="Loading…",
								ascii=False, ncols=75):
									time.sleep(0.01)
								if stage7=='1':
									print("FAIL\nYou just tried to fly out using the cannon, but it blasted you right into the wall. \nTo retry, rerun the whole program.")
								elif stage7=='2':
									print("FAIL\nYou just ate some cheese, and the chatting guards noticed you. Seems like you're under arrest. \nTo retry, rerun the whole program.")
								elif stage7=='3':
									stage8=input("-------------------------------STAGE 8--------------------------------\nYou flinged urself and the diamond, and luckily, ya both landed in some hay, without the guards noticing you.\n You have exited the museum. \nBut wait, there is one last guard you need to take down.\nYou can: Snap his neck{1}, Jump dow{2}, drop the diamond on his head{3}, or shoot him with a rifle{4}\n So whatcha gonna do: ")
									if stage8=='1':
										print("FAIL\nYou tried to snap his neck, but you lost your balance and fell down the stairs in front of you. \nTo retry, rerun the whole program.")
									elif stage8=='2':
										print("FAIL\nYou stole his rifle and tried to shoot him, but all your bullets missed him. Man, those first person shooters make it look easy. \nTo retry, rerun the whole program.")
									elif stage8=='4':
										print("FAIL\nYou jumped with the diamond but the diamond was too heavy and so you didn't get too far with that jump. Looks like you're under arrest. \nTo retry, rerun the whole program.")
									elif stage8=='3':
										for i in tqdm (range (101),
										desc="Loading…",
										ascii=False, ncols=75):
											time.sleep(0.1)
									print("-------------------------------YOU WON--------------------------------\nRANK:\nUNSEEN BURGLAR\n")

		elif stage1=='2':
			print("-------------------------------STAGE 2--------------------------------\nYou have decided to bust in on your small scooter.")
			stage2=input("There are 3 guards in front of you. \nYou can either ram into them {1}, kick them {2}, or jump over them {3}. \nWhat would you like to do? ")
			for i in tqdm (range (101),
										desc="Loading…",
										ascii=False, ncols=75):
											time.sleep(0.01)
			if stage2=='2':
				print("FAIL\nYou kicked one of the guards but lost control of the scooter and rammed into a pillar. Well, you got one of the guards. \nTo retry, rerun the whole program.")
			elif stage2=='3':
				print("FAIL\nYou jumped of the scooter and fell right in front of the cops. \nTo retry, rerun the whole program.")
			elif stage2=='1':
				print("-------------------------------STAGE 3--------------------------------\nWoah! Ya just rammed into those dudes right into the museum.\n You went through one the doors in front of you so fast that the guard couldn't stop you.\nBut that guard has called for backup, and now you're in a room with old medivial armour. \n There are guards in front of you, and you can use any one of these three equipment to save yourself:\n- Shield{1}\n- Lance{2}\n- Flail{3}")
				stage3=input("So what are you gonna be using? ")
				for i in tqdm (range (101),
										desc="Loading…",
										ascii=False, ncols=75):
											time.sleep(0.01)
				if stage3=='2':
					print("FAIL\nThe lance was way too heavy and you fell of the scooter with it. Jousting is harder than it looks. \nTo retry, rerun the whole program.")
				elif stage3=='3':
					print("FAIL\nYou Picked up the flail but it got stuck with a boat hanging from the ceiling. You're Stuck with it. What were you thinking would happen? \nTo retry, rerun the whole program.")
				elif stage3=='1':
					print("-------------------------------STAGE 4--------------------------------\nGood choice! While the guards fired bullets on you you used the shield to defend yorself.\nYou're still on the scooter and you get past the guards easily.\nYou break the diamond's glass shield.\nNow you can either put the diamond in the basket{1}\n or attach it to the scooters end using a tow cable{2}.")
					stage4=input("The decision is upto you: ") 
					for i in tqdm (range (101),
										desc="Loading…",
										ascii=False, ncols=75):
											time.sleep(0.01)
					if stage4=='1':
						print("FAIL\nThe iamond did get into the basket, but it was so heavy that it tilted the scooter to the front and flung you off the scooter. Now you'd wish you payed more attention to your physics classes. \nTo retry, rerun the whole program.")
					elif stage4=='2':
						print("-------------------------------STAGE 4--------------------------------\nWell done! You smashed your way through the museum and out through the museum and now you're outside! \nBut its not over yet! The police are chasing you in a car. \nA policeman is trying to shoot you! You can either throw a stone on him{1}, or jump on to the branch of a tree{2}.")
						stage4=input("So what is your choice? ")
						for i in tqdm (range (101),
										desc="Loading…",
										ascii=False, ncols=75):
											time.sleep(0.01)
						if stage4=='2':
							print("FAIL\nYou're safe on the branch but the diamond is back with the cops. The cops hear you shout for help and take you to jail. \nTo retry, rerun the whole program.")
						elif stage4=='1':
							print("-------------------------------STAGE 5--------------------------------\nDid you just murder a cop? Well, maybe you shouldn't have because now there is another police car and a sniper in a helicopter.\nNow you have to save yourself from the sniper. You can either: \n{1} Use a sticky grenade or \n{2} Protect yourself in a bubble.")
							stage5=input("Pls don't mess up now, you've almost made it. What do you want to do? ")
							for i in tqdm (range (101),
										desc="Loading…",
										ascii=False, ncols=75):
											time.sleep(0.01)
							if stage5=='1':
								print("FAIL\nThe sticky grenade stuck to your hand and blew up. \nTo retry, rerun the whole program.")
							elif stage5=='2':
								print("-------------------------------STAGE 6--------------------------------\nOMG!!! The bubble rotected you from 3 shots and now you are under a tunnel heading towards the the bridge. No need to worry about the helicopter, it crashed into the top of the tunnel.\nBut the police car is still behind you. Watch out! You're on the bridge, but the bridge is broken, so you stop the scooter. \n[Another police car arrives.]\nYou can either: {1} Bribe the policeman to let you go, {2} Drop the diamond into the river, or {3} Accelerate the scooter to jump over the bridge.")
								stage6=input("Which option do you think is right? ")
								for i in tqdm (range (101),
										desc="Loading…",
										ascii=False, ncols=75):
											time.sleep(0.01)
								if stage6=='1':
									print("FAIL\nUsually bribing works, but this time it didn't. How odd. The policeman declared bribing as a crime and arrested you. \nTo retry, rerun the whole program.")
								elif stage6=='3':
									print("FAIL\nYou tried your best couldn't get tto far before the cops circled in on you. \nTo retry, rerun the whole program.")
								elif stage6=='2':
									print("-------------------------------STAGE 7--------------------------------\nYou pushed the diamond back and you along with your scooter fell off the bridge. \nYou floated far away and became unconsious.\nA few hours later you wake up and find yourself on the bank of the river and next to you is......the Giant Diamond!")
									for i in tqdm (range (101),
										desc="Loading…",
										ascii=False, ncols=75):
											time.sleep(0.1)
									print("-------------------------------YOU WON--------------------------------\nRANK:\nINTRUDER ON A SCOOTER\n")

		else:
			print('Error. If you want to start from beginning, just rerun the program.')		

	elif start=='a':
		exit()

	else:
		print('Error. Retry pls.')
