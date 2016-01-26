from random import randint

def beast_health_calc(mob_damage):
    global health
    global beast_health
    #print("You have {} health, your {} - {} and are dealt {} damage".format(health, beast, beast_life, mob_damage))
    if mob_damage % 2 == 0:
        damage1 = int(mob_damage / 2)
        damage2 = int(mob_damage / 2)
        health -= damage1
        beast_health -= damage2
    else:
        damage1 = int((mob_damage + 1) / 2)
        damage2 = int((mob_damage - 1) / 2)
        health -= damage1
        beast_health -= damage2
    if beast_health > 0:
        print("You took {} of the damage, your {} took {} of the damage...".format(damage1, beast, damage2))
        #input("You now have {} health, and your {} - {}".format(health, beast, beast_life))
    else:
        print("You took {} of the damage, your {} took {} of the damage and is now dead...".format(damage1, beast, damage2))
        #input("You now have {} health, and you are all on your own...".format(health))
        input("You are now all on your own...")

# Mob names
mob_variety = ['vampire', 'werewolf']

# Mob Classes
mob_class = ""

# Types of Super Spells
bonus_list_info = ['Summon Beast', 'Super Heal', 'Equip Weapon']
bonus_list = ['b', 'h', 'w']

axes = ['cleaving axe', 'hatchet', 'tomahawk', 'long-bearded axe']
maces = ['driftwood club', 'spiked club', 'stone hammer', 'war hammer', 'bladed mace', 'rock breaker', 'flanged mace', 'behemoth mace']
ranged_weapons = ['gun', 'pistol', 'rifle', 'bow', 'crossbow', 'shortbow', 'longbow', 'mechanical bow']
daggers = ['qama', 'kris', 'stabby-stabby', 'tanto', 'kukri', 'khanjali', 'katar', 'balisong', 'machete']
swords = ['celtic sword', 'gladius', 'spatha', 'longsword', 'an arming sword', 'curtana', 'viking sword', 'swiss sword', 'cutlass', 'smallsword', 'sabre', 'hunting sword', 'balisword']
weapon_types_dict = {'axe' : axes, 'mace' : maces, 'ranged weapon' : ranged_weapons, 'dagger' : daggers, 'sword' : swords}
weapon_types = ['axe', 'mace', 'ranged weapon', 'dagger', 'sword']

# Beasts
birds = ['an eagle', 'an osprey', 'kite', 'buzzard', 'hawk', 'harrier', 'vulture', 'falcon', 'an owl']
felines = ['tiger', 'lion', 'jaguar', 'leopard', 'lynx', 'cougar', 'cheetah', 'sabretooth']
canines = ['wolf', 'jackal', 'fox', 'hyena', 'dingo dog']
ungulates = ['horse', 'zebra', 'tapir', 'rhino', 'camel', 'warthog', 'hippo', 'giraffe', 'pronghorn', 'deer', 'moose', 'an elk', 'muntjac', 'buffalo', 'an ox', 'mountain goat', 'an elephant']
primates = ['monkey', 'macaque', 'baboon', 'gibbon', 'gorilla', 'chimpanzee']
beast_types_dict = {'birds of prey' : birds, 'felines' : felines, 'canines' : canines, 'ungulates' : ungulates, 'primates' : primates}
beast_types = ['birds of prey', 'felines', 'canines', 'ungulates', 'primates']



# Player super spells
my_bonus_list = {'b' : 1, 'h' : 1, 'w' : 1}
beast = ""
beast_type = ""
beast_health = 0
beast_min = 0
beast_max = 0

weapon = ""
weapon_type = ""
weapon_durability = 0
weapon_damage = 0
sword_amplifier = 0

# Player health
health = 100

# Mob kills counter
mobs_killed = 0

# Mob modifiers
mob_modifier_passive = 0
mob_debuff = 0

# Turn counter
turn = 0
turn_check = True
# The game itself
print("Welcome to my game!")

# Game DIFFICULTY
print("Choose a difficulty:")
print("- 'n' for 'normal'")
print("- 'h' for 'hard'")
print("- 'i' for 'impossible'")
difficulty = input(">> ")
if difficulty == 'n':
    input("The difficulty was set to 'noob'")
elif difficulty == 'h':
    input("The difficulty was set to 'so hard you wanna throw your computer outa the window'")
elif difficulty == 'i':
    input("The difficulty was set to 'impossible'...")
else:
    difficulty = "i"
    print("You tried to trick me?!Impossible difficulty it is...")
    input("The difficulty was set to 'impossible'...")

# Class choice
# input("Warriors have a shield, when they equip a weapon they get a second weapon, the shield is unequipped...")
# input("Hunters get a random beast every third encounter unless their beast is still alive and a random trap is activated upon every encounter...")
# input("Priest - super heal and normal heal effect their beast also...")
print()
print("Choose a class:")
print("- 'w' for warrior")
print("- 'h' for huhter")
print("- 'p' for priest")
your_class = input(">> ")
while your_class != 'w' and your_class != 'h' and your_class != 'p':
    your_class = input("That is not a valid class choice, please try again!\n>> ")

print("Your class was set to...")
if your_class == 'w':
    print("f***ing badass!")
elif your_class == 'h':
    print("pew pew!")
elif your_class == 'p':
    print("bubblewrap!")

# GAME BEGINS
while True:
    # Life check
    if health <= 0:
        print("Game Over!")
        break

    # Mob defining
    # Mob name generator
    mob = mob_variety[randint(0,len(mob_variety)-1)]
    mob_health = randint(7,14)
    if difficulty == 'n':
        mob_class_row = randint(1,7)
    elif difficulty == 'h':
        mob_class_row = randint(4,7)
    elif difficulty == 'i':
        mob_class_row = 7
    if mob_class_row > 3 and mob_class_row < 7:
        mob_class = "Elite"
    elif mob_class_row == 7:
        mob_class = "Boss"
    if mob_class == "Elite":
        mob_health += 3
    elif mob_class == "Boss":
        mob_health += 7

    # Printing
    input("A {} attacks you!".format(mob))
    if mob_class == "Elite":
        print("An Elite!")
    elif mob_class == "Boss":
        print("A Boss!")
    if beast_health > 0:
        input("You have {} health, your {} has {} health, the {} has {} health...".format(health, beast, beast_health, mob, mob_health))
    else:
        input("You have {} health, the {} has {} health...".format(health, mob, mob_health))
    print()

    # Mob fight
    while mob_health > 0:
        
        # Turn set
        turn += 1
        print("Turn {}".format(turn))
        your_heal = 0

        # Beast deals damage
        if turn_check == True:
            if beast_health > 0:
                beast_damage = randint(beast_min, beast_max)
                print("Your {} deals {} damage to the {}.".format(beast, beast_damage, mob))
                mob_health -= beast_damage
                if mob_health > 0:
                    input("The {} now has {} health left.".format(mob, mob_health))
                else:
                    input("Your {} killed the {} ...".format(beast, mob))
        else:
            turn_check = True

        # Decisions
        if mob_health > 0:
            print("Decide:")
            print("- 'a' to attack")
            print("- 'h' to heal")
            print("- 'c' to check your bag and spellbook")
            choice = input(">> ")
        else:
            choice = 0
        # Mob damage + passive/class modifiers
        
        mob_damage = randint(1,5) + mob_modifier_passive

        if mob_class == "Elite":
            mob_damage += 10
        elif mob_class == "Boss":
            mob_damage += 20

        # Player attack choice - mob damage and player damage
        if choice == "a":
            if weapon_type != "ranged weapon" or weapon_durability == 0:
                if mob_debuff == 0:
                    print("The {} deals {} damage...".format(mob, mob_damage))
                    if beast_health > 0:
                        beast_health_calc(mob_damage)
                    else:
                        health -= mob_damage
                else:
                    input("The {} is {} and cannot attack you this turn...".format(mob, mob_debuff))
                    mob_debuff = 0
            else:
                print("You shoot from a distance with your {}, the {} can't attack you.".format(weapon, mob))
            
            if weapon_durability > 0:
                your_damage = randint(3,7) + weapon_damage
            else:
                your_damage = randint(3,7)

            if weapon_type == "axe" and weapon_durability > 0:
                if mob_health > weapon_damage:
                    input("You swing your {} and deal {} damage to the {}...".format(weapon, weapon_damage, mob))
                else:
                    input("You swing your {} and chop the {}'s head off...".format(weapon, mob))
                mob_health -= weapon_damage
            elif weapon_type == "mace" and weapon_durability > 0:
                if your_damage < mob_health:
                    input("You slam the {} who is now stunned by your {}...".format(mob, weapon))
                    mob_debuff = "stunned"
                else:
                    input("You crush the {}'s head with your {}...".format(mob, weapon))
            elif weapon_type == "ranged weapon":
                if your_damage < mob_health:
                    print("You shot the {}'s body with your {}.".format(mob, weapon))
                else:
                    print("You hit the bullseye... the {} is dead!".format(mob))
            elif weapon_type == "sword" and weapon_durability > 0:
                #sword_amplifier = 3
                sword_amplifier = randint(1,3)
                if sword_amplifier == 1:
                    weapon_durability -= 1
                    if weapon_durability > 0:
                        input("You cut the {} dealing {} damage with your {} which now has {} durability left...".format(mob, your_damage, weapon, weapon_durability))
                    else:
                        input("You cut the {} dealing {} damage with your {}...".format(mob, your_damage, weapon))
                elif sword_amplifier == 2:
                    your_damage *= 2
                    weapon_durability -= 2
                    if weapon_durability > 0:
                        input("You slice through the {}'s body dealing {} damage with your {} which now has {} durability left...".format(mob, your_damage, weapon, weapon_durability))
                    else:
                        input("You slice through the {}'s body dealing {} damage with your {} which is now blunt...".format(mob, your_damage, weapon))
                elif sword_amplifier == 3:
                    input("You slice the {}'s head off with your {} which is now blunt...".format(mob, weapon))
                    your_damage *= 7
                    weapon_durability = 0
            elif weapon_type == "dagger" and weapon_durability > 0:
                if your_damage >= mob_health:
                    input("You stabbed the {} to death with your {}...".format(mob, weapon))
                else:
                    if weapon_durability - 1 <= 0:
                        print("You stabbed the {} who now has {} health with your {}.".format(mob, mob_health - your_damage, weapon))                    
                    elif weapon_durability - 1 > 0:
                        print("You stabbed the {} who now has {} health with your {} which now has {} durability left.".format(mob, mob_health - your_damage, weapon, weapon_durability - 1))
                        print("Do you stab again?")
                        print("- 'y' for yes")
                        print("- 'n' for no")
                        second_stab = input(">> ")
                        while second_stab != 'y' and second_stab != 'n':
                            second_stab = input(">> ")
                        if second_stab == 'y':
                            weapon_durability -= 1
                            your_damage += randint(3,7) + weapon_damage
                            if your_damage >= mob_health:
                                input("You stabbed the {} to death with your {}...".format(mob, weapon))
                            else:
                                print("You stabbed the {} who now has {} health with your {}.".format(mob, mob_health - your_damage, weapon))
                                   
            # In case Player has no weapon
            if weapon_durability <= 0 and mob_health > your_damage:
                input("You deal {} damage...".format(your_damage))

            elif weapon_durability <= 0 and mob_health <= your_damage:
                input("You kill the {} mercilessly".format(mob))

            # In case Player has weapon
            elif weapon_durability > 0 and sword_amplifier == 0 and mob_health > your_damage:
                weapon_durability -= 1
                if weapon_durability == 0:
                    input("You deal {} damage total with your {}...".format(your_damage, weapon))
                    input("Your {} is now blunt and is no longer useful.".format(weapon))
                else:
                    input("You deal {} damage total with your {} which now has {} durability left...".format(your_damage, weapon, weapon_durability))
            elif weapon_durability > 0 and sword_amplifier == 0 and mob_health <= your_damage:
                weapon_durability -= 1
                if weapon_durability == 0:
                    input("Your {} is now blunt and is no longer useful.".format(weapon))
                else:
                    input("Your {} now has {} durability left...".format(weapon, weapon_durability))
            else:
                weapon_durability == 0

            mob_health -= your_damage
            sword_amplifier = 0
            #print("You have {} durability".format(weapon_durability))

        # Player heal choice, can't overheal - player heal and mob damage
        elif choice == 'h':
            your_heal = randint(2,60)
            health += your_heal
            if health > 100:
                overheal = health - 100
                health = health - your_heal
                input("You heal yourself with {}, {} overheal...".format(your_heal, overheal))
            elif your_heal > 0:
                input("You heal yourself with {}...".format(your_heal))
                

            #print("My health is {}, my beast's health is {}".format(health, beast_life))
            if mob_debuff == 0:
                print("The {} deals {} damage...".format(mob, mob_damage))
                if beast_health > 0:
                    beast_health_calc(mob_damage)
                else:
                    health -= mob_damage
            else:
                input("The {} is {} and cannot attack you this turn...".format(mob, mob_debuff))
                mob_debuff = 0
                
            if weapon_type == "axe" and weapon_durability > 0:
                weapon_durability -= 1
                if weapon_durability > 0 and mob_health > weapon_damage:
                    input("You swing your {} and deal {} damage to the {}... {} durability left".format(weapon, weapon_damage, mob, weapon_durability))
                elif weapon_durability > 0:
                    input("You swing your {} and chop the {}'s head off... {} durability left".format(weapon, mob, weapon_durability))
                elif weapon_durability == 0 and mob_health > weapon_damage:
                    input("You swing your {} and deal {} damage to the {}...".format(weapon, weapon_damage, mob))
                    input("Your {} broke...".format(weapon))
                else:
                    input("You swing your {} and chop the {}'s head off...".format(weapon, mob))
                    input("Your {} broke...".format(weapon))
                mob_health -= weapon_damage

        # Player spell choice
        elif choice == 'c':
            # Spell check
            print("You have {} spells in your spellbook and {} weapons in your bag:".format(my_bonus_list['b'] + my_bonus_list['h'], my_bonus_list['w']))
            print("- 'Summon Beast' : {} left.".format(my_bonus_list['b']))
            print("- 'Super Heal' : {} left.".format(my_bonus_list['h']))
            print("- 'Equip Weapon' : {} left.".format(my_bonus_list['w']))
            print()

            # If Player has no spells
            if my_bonus_list['b'] == 0 and my_bonus_list['h'] == 0 and my_bonus_list['w'] == 0:
                input("Sorry, you don't have any super spells left...")
                turn_check = False
                turn -= 1

            # If Player has spells
            else:
                print("Press ENTER to continue or choose:")
                print("- 'b' for Summon Beast")
                print("- 'h' for Super Heal")
                print("- 'w' for Equip Weapon")
                choice = input(">> ")
                if choice == 'b' or choice == 'h' or choice == 'w':
                    # Choice validity check
                    try:
                        while my_bonus_list[choice] == 0:
                            input("You don't have any of that spell left.")
                            choice = input("Choose something else or press ENTER to continue with the game...")
                            
                        # Change of mind handler
                        if choice == "":
                            input("The game will reset this turn...")
                            turn_check = False
                            turn -= 1
                        elif choice == 'b':
                            # Define Beast
                            beast_type = beast_types[randint(0,len(beast_types)-1)]
                            beast = beast_types_dict[beast_type][randint(0,len(beast_types_dict[beast_type])-1)]
                            beast_health = randint(1,5) * 10
                            beast_min = randint(1,3)
                            beast_max = randint(7,10)

                            # Inform Player
                            if beast[0] != "a":
                                print("You summoned a {} from the woods with {} life which deals between {} and {} damage.".format(beast, beast_health, beast_min, beast_max))
                            else:
                                print("You summoned {} from the woods with {} life which deals between {} and {} damage.".format(beast, beast_health, beast_min, beast_max))
                                beast = beast[3:]
                            input("{}{} is from the {}{} family".format(beast[0].upper(), beast[1:], beast_type[0].upper(), beast_type[1:]))
                            print(beast)
                            my_bonus_list[choice] -= 1
                        elif choice == 'h':
                            print("Super Heal is between 50 and 150, and it doesn't overheal.")
                            super_heal = randint(50,150)
                            health += super_heal
                            input("casting...")
                            print("You now have +{} health".format(super_heal))
                            my_bonus_list[choice] -= 1
                        elif choice == 'w':
                            # Define Weapon
                            weapon_type = weapon_types[randint(0,len(weapon_types)-1)]
                            weapon = weapon_types_dict[weapon_type][randint(0,len(weapon_types_dict[weapon_type])-1)]
                            weapon_durability = randint(2,5)
                            weapon_damage = randint(3,7)
                            # Inform Player
                            if weapon[0] != "a":
                                print("You equipped a {} from your bag with {} durability which gives you +{} damage.".format(weapon, weapon_durability, weapon_damage))
                            else:
                                print("You equipped {} from your bag with {} durability which gives you +{} damage.".format(weapon, weapon_durability, weapon_damage))
                                weapon = weapon[3:]
                            input("{}{} is type {} weapon...".format(weapon[0].upper(), weapon[1:], weapon_type))
                            print(weapon)
                            my_bonus_list[choice] -= 1

                    # Error + change of mind handler
                    except KeyError:
                        input("Either you wanted to continue or your choice was invalid, the game will reset this turn anyway...")
                        turn_check = False
                        turn -= 1

                # Change of mind handler
                elif choice == "":
                    input("The game will reset this turn...")
                    turn_check = False
                    turn -= 1
                # Invalid choice handler
                else:
                    input("That's not a valid choice...")
                    input("The game will reset this turn...")
                    turn_check = False
                    turn -= 1
        elif choice == 0:
            if mob_class == "Boss":
                beast_health += 10
            beast_health += randint(5,15)
            print("You feed your {}, which now has {} health.".format(beast, beast_health))
        # Invalid choice - mob still attacks
        else:
            if mob_debuff == 0:
                input("You panick! The {} deals {} damage and laughs at you...".format(mob, mob_damage))
                if beast_health > 0:
                    beast_health_calc(mob_damage)
                else:    
                    health -= mob_damage
            else:
                input("The {} is {} and cannot attack you this turn...".format(mob, mob_debuff))
                mob_debuff = 0
            
        # Turn results check
        # Player life check
        if health <= 0:
            input("Your health is 0...")
            break

        # Mob life check
        elif mob_health > 0:
            if beast_health <= 0:
                print("Your health is {}, the {}'s health is {}.".format(health, mob, mob_health))
            else:
                print("Your health is {}, your {}'s health is {}, the {}'s health is {}.".format(health, beast, beast_health, mob, mob_health))
        # In case mob is dead
        else:
            mob_debuff = 0
            if beast_health <= 0:
                input("Your health is {}, the {} is dead!".format(health, mob))
            else:
                input("Your health is {}, your {}'s health is {}, the {} is dead!".format(health, beast, beast_health, mob))
            mobs_killed += 1
            if mobs_killed == 1:
                print ("{} monster killed".format(mobs_killed))
            else:
                print ("{} monsters killed".format(mobs_killed))

            # Mob passive modifier increase
            if mob_modifier_passive < 30 and mobs_killed % 3 == 0:
                mob_modifier_passive += 1
                print("Enemies grow in strength.")

            # Every 5 mob kills grant a random super spell
            if mobs_killed % 5 == 0 or mob_class == "Boss":
                random_bonus = randint(0, len(bonus_list) - 1)
                my_bonus_list[bonus_list[random_bonus]] += 1
                print("1 {} was added to your spellbook.".format(bonus_list_info[random_bonus]))

        # Turn Spacing
        print()

# Super heal + heal bug
# Summon beast is useless while you have a beast
# Bosses don't have enough health
