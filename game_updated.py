from random import randint
#  IMPORTANT
"""
def boss_effects(mob):
    if boss_switch == False and mob_class == "Boss":
        if mob == 'Dracula':
            mob_health += int(mob_damage / 2)
        elif mob == 'Godzilla':
            mob_damage += int(mob_damage / 3)
        elif mob == 'Freddy Krueger':
"""            
#def weapon_mechanism(durability, weapon_type, choice):

def priest_mechanism():
    if randint(1,3) != 2:
        input("You manage to cast a quick heal in the heat of the battle...")
        heal_mechanism()

def hunter_mechanism():
    global trap_potency
    global trap_spring
    global mob
    global mob_debuff
    
    if trap_potency > 0 and trap_spring == False:
        choice = input("You have set a trap before the battle began\nDecide:\n- 'y' to use it\n- 'n' to NOT use it\n>>")
        print()
        if choice == 'y':
            trap_spring = True
            input("You lead {} into a trap...".format(mob))
            mob_debuff = "is entrapped"
            if 0 < trap_potency and trap_potency < 4:
                input("Trap potency is 1 turn")
                trap_potency = 0
            elif 3 < trap_potency and trap_potency < 6:
                input("Trap potency is 2 turns")
                trap_potency = 1
            elif trap_potency == 7:
                input("Trap potency is 3 turns")
                trap_potency = 2
            
    elif trap_potency > 0 and trap_spring == True:
        trap_potency -= 1
        if trap_potency == 0:
            print("Trap recovery is next turn")
            mob_debuff = "is entrapped, but will recover next turn".format(trap_potency)
        else:
            mob_debuff = "is entrapped, but will recover in {} turns".format(trap_potency)

def warrior_mechanism():
    global block

    block_chance = randint(1,7) ######################################################################################
    print("Block chance = {}".format(block_chance)) ####################################################################################
    if block_chance == 7:
        block = True
    #elif block_chance > 3:
    #    block = 3
    #else:
    #    block = 2
    #print("Block = {}".format(block)) ####################################################################################
        
def class_mechanism():
    global your_class
    
    if your_class == 'w':
        warrior_mechanism()
    elif your_class == 'h':
        hunter_mechanism()
    elif your_class == 'p':
        priest_mechanism()
    #else:####################################################################################
        
def beast_mechanism(case):
    global health
    global beast_health
    global mob
    global mob_damage
    global beast_min
    global beast_max
    global mob_modifier
    global mob_health

    if case == False:
        if beast_health > 0:
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

            # Inform player
            print("{}{} deals {} damage...".format(mob[0].upper(), mob[1:], mob_damage))
            if beast_health > 0:
                print("You took {} of the damage, your {} took {} of the damage...".format(damage1, beast, damage2))
            else:
                print("You took {} of the damage, your {} took {} of the damage and {} is now dead...".format(damage1, beast, damage2, beast))
                input("You are now all on your own...")
        else:
            print("{}{} deals {} damage to you...".format(mob[0].upper(), mob[1:], mob_damage))
            health -= mob_damage
    else:
        beast_damage = randint(beast_min, beast_max) + int(mob_modifier_passive / 3)
        mob_health -= beast_damage
        print("Your {} deals {} damage to {}.".format(beast, beast_damage, mob))
        if mob_health > 0:
            input("{}{} now has {} health left.".format(mob[0].upper(), mob[1:], mob_health))
        else:
            input("Your {} killed {}...".format(beast, mob))

def attack_mechanism(case, your_damage):
    global mob
    global mob_health
    global mob_debuff
    global block
    global mob_modifier_passive
    
    if your_damage > 0:
        mob_health -= your_damage    
    if case == True:
        beast_mechanism(case)
    if mob_debuff == False:
        if block == False:
            beast_mechanism(case)
        elif block == True:
            print(block)
            block = False
            print(block)
            input("{}{} attacked you from behind, but you managed to block all {} damage with your shield...".format(mob[0].upper(), mob[1:], randint(10,30) + mob_modifier_passive))
    elif mob_debuff != False and case == False:
        input("{}{} is {} and cannot attack you this turn...".format(mob[0].upper(), mob[1:], mob_debuff))
        mob_debuff = False
        
def weapon_axe(choice, your_damage):
    global mob
    global weapon
    global mob_health

    if choice == 'a':
        meta_damage = your_damage + randint(12, 24)
        if meta_damage < mob_health:
            input("You strike {} with your {}...".format(mob, weapon))
        else:
            input("You swing your {} and chop {}'s head off...".format(weapon, mob))
        return meta_damage
    elif choice == 'h':
        meta_damage = randint(3, 12)
        mob_health -= meta_damage
        if mob_health > 0:
            input("You swing your {} dealing {} damage to {}".format(weapon, meta_damage, mob))
        else:
            input("You swing your {} and chop {}'s head off...".format(weapon, mob))
    else:
        return False

def weapon_mace(choice, your_damage):
    global mob
    global weapon
    global mob_health
    
    if choice == 'a_post':
        return "stunned"
    elif choice == 'a':
        meta_damage = your_damage + randint(3, 7) * 3
        if meta_damage < mob_health:
            input("You slam {} who is now stunned by your {}...".format(mob, weapon))
        else:
            input("You crush {}'s head with your {}...".format(mob, weapon))
        return meta_damage
    else:
        return False

def weapon_ranged(choice, your_damage):
    global mob
    global weapon
    global mob_health

    if choice == 'a_prep':
        return "too far away"
    elif choice == 'a':
        meta_damage = your_damage + randint(10, 20)
        if meta_damage < mob_health:
            print("You shot through {}'s body with your {}.".format(mob, weapon))
        else:
            print("You hit the bullseye... {} is dead!".format(mob))
        return meta_damage
    else:
        return False

def weapon_dagger(choice, your_damage):
    global mob
    global weapon
    global mob_health
    
    if choice == 'a':
        meta_damage = your_damage + randint(3,7)
        if meta_damage < mob_health:
            print("You stabbed {} with your {}".format(mob, weapon))
            print("Do you stab again?")
            print("- 'y' for yes")
            print("- 'n' for no")
            second_stab = input(">> ")
            while second_stab != 'y' and second_stab != 'n':
                second_stab = input(">> ")
            if second_stab == 'y':
                meta_damage += randint(7,24)
                if your_damage >= mob_health:
                    input("You stabbed {} to death with your {}...".format(mob, weapon))
                else:
                    print("You stabbed {} in the eye with your {}, dealing {}.".format(mob, weapon, meta_damage))
        else:
            input("You stabbed {} to death with your {}...".format(mob, weapon))
        return meta_damage
    else:
        return False

def weapon_sword(choice, your_damage):
    global mob
    global weapon
    global mob_health
    
    if choice == 'a':
        meta_damage = your_damage
        sword_amplifier = randint(1,3)
        if sword_amplifier == 1:
            meta_damage *= 3
            input("You cut {} with your {}...".format(mob, weapon))
        elif sword_amplifier == 2:
            meta_damage *= 7
            if meta_damage < mob_health:
                input("You slice through {}'s body dealing {} damage with your {}...".format(mob, meta_damage, weapon))
            else:
                input("You slice through {}'s body dealing {} damage, shredding {} into pieces with your {}...".format(mob, meta_damage, mob, weapon))
        elif sword_amplifier == 3:
            meta_damage *= 100
            input("You slice {}'s head off with your {}...".format(mob, weapon))
        return meta_damage
    else:
        return False

def weapon_mechanism(choice, your_damage):
    global weapon_type
    global weapon_durability
    
    if weapon_type == 'axe':
        return weapon_axe(choice, your_damage)
    elif weapon_type == 'mace':
        return weapon_mace(choice, your_damage)
    elif weapon_type == 'ranged weapon':
        return weapon_ranged(choice, your_damage)
    elif weapon_type == 'dagger':
        return weapon_dagger(choice, your_damage)
    elif weapon_type == 'sword':
        return weapon_sword(choice, your_damage)
    else:
        return False

def durability_mechanism(your_damage):
    global weapon_durability
    global mob_health
    global weapon
    
    if mob_health > 0:
        if weapon_durability == 0:
            input("You deal {} damage total with your {}...".format(your_damage, weapon))
            input("Your {} is now blunt and no longer useful.".format(weapon))
        else:
            input("You deal {} damage total with your {} which now has {} durability left...".format(your_damage, weapon, weapon_durability))
    else:
        if weapon_durability == 0:
            input("Your {} is now blunt and is no longer useful...".format(weapon))
        else:
            input("Your {} now has {} durability left...".format(your_damage, weapon, weapon_durability))

def heal_mechanism():
    global beast_health
    global health
    global beast

    your_heal = randint(5,30) * 2
    if beast_health > 0:
        health += int(your_heal / 2)
        beast_health += int(your_heal / 2)
        input("You heal yourself with {} and your {} with {}...".format(int(your_heal / 2), beast, int(your_heal / 2)))
    else:
        health += your_heal
        input("You heal yourself with {}...".format(your_heal))
    if health > 1000:
        health = 1000
        input("1000 health is the limit...")

def no_spells():
    global turn_check
    global turn
    global my_bonus_list
    
    if my_bonus_list['b'] == 0 and my_bonus_list['h'] == 0 and my_bonus_list['w'] == 0:
        input("Sorry, you don't have any super spells left...")
        turn_check = False
        turn -= 1
        return True
def summon_beast_mechanism():
    global beast
    global beast_type
    global beast_types
    global beast_types_dict
    global beast_health
    global beast_min
    global beast_max
    global mob_modifier
    global my_bonus_list
    
    # Define Beast
    beast_type = beast_types[randint(0,len(beast_types)-1)]
    beast = beast_types_dict[beast_type][randint(0,len(beast_types_dict[beast_type])-1)]
    beast_health = randint(1,5) * 10 + mob_modifier_passive
    beast_min = randint(1,3)
    beast_max = randint(7,10)

    # Inform Player
    if beast[0] != "a":
        print("You summoned a {} from the woods with {} life which deals between {} and {} damage.".format(beast, beast_health, beast_min, beast_max))
    else:
        print("You summoned {} from the woods with {} life which deals between {} and {} damage.".format(beast, beast_health, beast_min, beast_max))
        beast = beast[3:]
    input("{}{} is from the {}{} family".format(beast[0].upper(), beast[1:], beast_type[0].upper(), beast_type[1:]))
    #print(beast)
    my_bonus_list['b'] -= 1

def super_heal_mechanism():
    global health
    global my_bonus_list
    global beast_health
    global beast
    
    print("Super Heal is between 100 and 300. If you have a beast, it is shared")
    super_heal = randint(50,150)
    input("casting...")
    if beast_health > 0:
        health += super_heal
        beast_health += super_heal
        print("+{} health for you and for your {}!".format(super_heal, beast))
    else:
        health += super_heal * 2
        print("+{} health!".format(super_heal * 2))
    my_bonus_list['h'] -= 1

def equip_weapon_mechanism():
    global weapon
    global weapon_type
    global weapon_types
    global weapon_types_dict
    global weapon_durability
    global weapon_damage
    global my_bonus_list
    global mob_modifier_passive
    
    # Define Weapon
    weapon_type = weapon_types[randint(0,len(weapon_types)-1)]
    weapon = weapon_types_dict[weapon_type][randint(0,len(weapon_types_dict[weapon_type])-1)]
    weapon_durability = randint(3,5) + mob_modifier_passive // 14
    weapon_damage = randint(3,7)
    # Inform Player
    if weapon[0] != "a":
        print("You equipped a {} from your bag with {} durability which gives you +{} damage.".format(weapon, weapon_durability, weapon_damage))
    else:
        print("You equipped {} from your bag with {} durability which gives you +{} damage.".format(weapon, weapon_durability, weapon_damage))
        weapon = weapon[3:]
    if weapon_type == "ranged weapon":
        input("{}{} is type {} ...".format(weapon[0].upper(), weapon[1:], weapon_type))
    else:
        input("{}{} is type {} weapon...".format(weapon[0].upper(), weapon[1:], weapon_type))
    # print(weapon)
    my_bonus_list['w'] -= 1

def choice_a():
    global weapon_durability
    global mob_health
    global mob_debuff
    global weapon_damage
    
    your_damage = randint(3,7)
    if weapon_durability > 0:
        your_damage += weapon_damage
        mob_debuff = weapon_mechanism('a_prep', your_damage)
        print('mob debuff is {}'.format(mob_debuff))
        your_damage = weapon_mechanism('a', your_damage)
        weapon_durability -= 1
        durability_mechanism(your_damage)
    else:
        if your_damage < mob_health:
            input("You deal {} damage...".format(your_damage))
        else:
            input("You kill {} mercilessly".format(mob)) ####################### HOW? variety
    attack_mechanism(False, your_damage)
    your_damage = 0
    mob_debuff = weapon_mechanism('a_post', your_damage)
def choice_h():
    heal_mechanism()
    attack_mechanism(False, 0)
    if weapon_durability > 0:
        weapon_mechanism('h', 0)
def choice_c():
    global turn
    global turn_check
    global my_bonus_list

    check = no_spells()
    if check != True:
        # Spell check
        print("You have {} spells in your spellbook and {} weapons in your bag:".format(my_bonus_list['b'] + my_bonus_list['h'], my_bonus_list['w']))
        print("- 'Summon Beast' : {} left.".format(my_bonus_list['b']))
        print("- 'Super Heal' : {} left.".format(my_bonus_list['h']))
        print("- 'Equip Weapon' : {} left.".format(my_bonus_list['w']))
        print()
        print("Press ENTER to reset this turn or choose:")
        print("- 'b' for Summon Beast")
        print("- 'h' for Super Heal")
        print("- 'w' for Equip Weapon")
        choice = input(">> ")
        while choice != 'b' and choice != 'h' and choice != 'w' and choice != '':
            choice = input("Invalid choice\n>>")
            
        if choice == '':
            input("The game will reset this turn...")
            turn_check = False
            turn -= 1
        elif choice == 'b':
            summon_beast_mechanism()
        elif choice == 'h' and my_bonus_list[choice] != 0:
            super_heal_mechanism()
        elif choice == 'w' and my_bonus_list[choice] != 0:
            equip_weapon_mechanism()
""" 
            print("Press ENTER to reset this turn or choose:")
            print("- 'b' for Summon Beast")
            print("- 'h' for Super Heal")
            print("- 'w' for Equip Weapon")
            choice = input(">> ")
                     
            # Change of mind handler
            if choice == "":
                input("The game will reset this turn...")
                turn_check = False
                turn -= 1

            elif choice == 'b' and my_bonus_list[choice] != 0:
                print("try")
                summon_beast_mechanism()
            elif choice == 'h' and my_bonus_list[choice] != 0:
                super_heal_mechanism()
            elif choice == 'w' and my_bonus_list[choice] != 0:
                equip_weapon_mechanism()
            else:
                print("Wrong input, try again:\n>>")
"""

def choice_false():
    global beast
    global beast_health
    global mob_class
    global mob_modifier_passive
    
    if mob_class == "Boss":
        beast_health += 70 + mob_modifier_passive
    beast_health += randint(10, 30)
    print("You feed your {}, which now has {} health.".format(beast, beast_health))
def choice_else():
    if mob_debuff == False:
        input("You panick!")
        attack_mechanism(False, 0)

def choice_mechanism(choice):
    if choice == 'a':
        choice_a()
    elif choice == 'h':
        choice_h()
    elif choice == 'c':
        choice_c()
    elif choice == False:
        choice_false()
    else:
        choice_else()

def random_bonus_funct():
    global my_bonus_list
    global bonus_list_info
    random_bonus = randint(0, len(bonus_list) - 1)
    my_bonus_list[bonus_list[random_bonus]] += 1
    return bonus_list_info[random_bonus]

def beast_health_calc(mob_damage):
    global health
    global beast_health
    global mob
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
        print("You took {} of the damage, your {} took {} of the damage and {} is now dead...".format(damage1, beast, damage2, mob))
        #input("You now have {} health, and you are all on your own...".format(health))
        input("You are now all on your own...")

# Mob names
mob_variety = ['the vampire', 'the werewolf', 'the minotaur', 'the titan', 'the shapeshifter', 'the wraith', 'the reaper', 'the ghoul', 'the wendigo', 'the predator', 'the xenomorph', 'the gremlin']
#mob_variety_boss = ['Dracula', 'William, the lycan lord', 'ManBearPig', 'the Grim Reaper', 'Godzilla', 'King Kong', 'Frankenstein', 'Kraken', 'Basilisk', 'the Loch Ness Monster', 'Stay Puft Marshmallow Man', 'Chucky', 'Freddy Krueger', 'Jason Vorhees', 'the Babadook', 'Kaiju', 'the Mummy']
mob_variety_boss = ['Freddy Krueger', 'Jason Vorhees']
# Mob Classes
mob_class = ""

# Sceneries

scenery_list = ['a dungeon', 'a forest', 'a village', 'a city', 'a mountain', 'a wooden bridge', 'a labyrinth']

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

weapon = "manticore" ###########################################################################################################
weapon_type = "ranged weapon" ###########################################################################################################
weapon_durability = 100 ###########################################################################################################
weapon_damage = 5 ###########################################################################################################
sword_amplifier = 0

# Player health and modifiers
health = 100
hero_debuff = False
block = False

# Mob kills counter
mobs_killed = 0

# Mob modifiers
boss_switch = False
mob_modifier_passive = 35 ###########################################################################################################
mob_debuff = False

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
difficulty = input(">> ").lower()
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
print("- 'w' for Warrior")
print("- 'h' for Hunter")
print("- 'p' for Priest")
your_class = input(">> ").lower()
while your_class != 'w' and your_class != 'h' and your_class != 'p':
    your_class = input("That is not a valid class choice, please try again!\n>> ")

print("Your class was set to...")
if your_class == 'w':
    print("warrior!")
elif your_class == 'h':
    print("pew pew!")
elif your_class == 'p':
    print("priest!")

# GAME BEGINS
while True:
    # Life check
    if health <= 0:
        print("Game Over!")
        break

    # Mob defining
    # Mob name generator
    mob = mob_variety[randint(0,len(mob_variety)-1)]
    mob_health = randint(7,14) + mob_modifier_passive * 3

    # Difficulty check
    if difficulty == 'n':
        mob_class_roll = randint(1,7)
    elif difficulty == 'h':
        mob_class_roll = randint(4,7)
    elif difficulty == 'i':
        mob_class_roll = 7

    # Chooses mob_class with chance according to difficulty
    if mob_class_roll > 3 and mob_class_roll < 7:
        mob_class = "Elite"
        mob_health += 3
    elif mob_class_roll == 7:
        mob_class = "Boss"
        mob_health += 7

    # Storytelling
    scenery = scenery_list[randint(0, len(scenery_list) - 1)]
    variety = randint(1,3)
    if variety == 1 and (mob_class != "Boss" or boss_switch == True):
        input("While you are crossing {}, a {} attacks you from behind!".format(scenery, mob[4:]))
    elif variety == 2 and (mob_class != "Boss" or boss_switch == True):
        input("You find a {} lurking in {}".format(mob[4:], scenery))
    elif variety == 3 and (mob_class != "Boss" or boss_switch == True):
        input("You find a {} lurking in {}".format(mob[4:], scenery))

    # Mob defining
    if mob_class == "Elite":
        print("An Elite!")
    elif mob_class == "Boss":
        if boss_switch == False:
            boss_index = randint(0, len(mob_variety_boss) - 1)
            mob = mob_variety_boss[boss_index]
            input("You finally found {}.".format(mob, mob, scenery))
        else:
            print("A Boss!!!")
    if beast_health > 0:
        input("You have {} health, your {} has {} health, {} has {} health...".format(health, beast, beast_health, mob, mob_health))
    else:
        input("You have {} health, {} has {} health...".format(health, mob, mob_health))
    print()
    
    # Trap defining // set if hunter
    trap_potency = randint(1,7)
    print("trap potency is {}".format(trap_potency))
    trap_spring = False
    
    
    # Mob fight
    while mob_health > 0:
        
        # Turn set
        turn += 1
        print("Turn {}".format(turn))

        # Class Skills
        class_mechanism()
        
        # Beast deals damage
        if turn_check == True:
            if beast_health > 0:
                beast_damage = randint(beast_min, beast_max) + int(mob_modifier_passive / 3)
                print("Your {} deals {} damage to {}.".format(beast, beast_damage, mob))
                mob_health -= beast_damage
                if mob_health > 0:
                    input("{}{} now has {} health left.".format(mob[0].upper(), mob[1:], mob_health)) ############################################## CHECKKKK
                else:
                    input("Your {} killed {}...".format(beast, mob))
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
            choice = False
        # Mob damage + passive/class modifiers
        
        mob_damage = randint(1,3) + mob_modifier_passive

        if mob_class == "Elite":
            mob_damage += 7
        elif mob_class == "Boss":
            mob_damage += 10

        # Player attack choice - mob damage and player damage
        if choice == "a":
            choice_a()
            
        # Player heal choice, can't overheal - player heal and mob damage
        elif choice == 'h':
            choice_h()

        # Player spell choice
        elif choice == 'c':
            choice_c()
        
        elif choice == False:
            choice_false()
        # Invalid choice - mob still attacks
        else:
            choice_else()
            
        # Turn results check
        # Player life check
        if health <= 0:
            input("Your health is 0...")
            break

        # Mob life check
        elif mob_health > 0:
            mob_debuff = False
            if beast_health <= 0:
                print("Your health is {}, {}'s health is {}.".format(health, mob, mob_health))
            else:
                print("Your health is {}, your {}'s health is {}, {}'s health is {}.".format(health, beast, beast_health, mob, mob_health))
        # In case mob is dead
        else:
            mob_debuff = False
            if beast_health <= 0:
                input("Your health is {}, {} is dead!".format(health, mob))
            else:
                input("Your health is {}, your {}'s health is {}, {} is dead!".format(health, beast, beast_health, mob))
            mobs_killed += 1
            if mobs_killed == 1:
                print ("{} monster killed".format(mobs_killed))
            else:
                print ("{} monsters killed".format(mobs_killed))

            # Mob passive modifier increase
            if mob_modifier_passive < 35 and mobs_killed % 2 == 0: # or boss
                mob_modifier_passive += 1
                print("Enemies grow in strength.")

            luck = randint(1,3)
            if luck == 3:
                print("1 {} was added to your spellbook because you are lucky".format(random_bonus_funct()))
            # Every 5 mob kills grant a random super spell
            if mobs_killed % 3 == 0:
                print("1 {} was added to your spellbook.".format(random_bonus_funct()))
            if mob_class == "Boss":
                if boss_switch == False:
                    print("QUEST COMPLETE:")
                    input("{}{} was heroicly killed by you...".format(mob[0].upper(), mob[1:]))
                    mob_variety_boss.pop(boss_index)
                    print(mob_variety_boss) ###########################################################################################################
                print("1 {} was added to your spellbook as a reward for killing {}.".format(random_bonus_funct(), mob))
                if len(mob_variety_boss) == 0 and boss_switch == False:
                    print(boss_switch)
                    boss_switch = True
                    print("All quests complete {}".format(boss_switch))

        
        # Turn Spacing
        print()

# Super heal + heal bug
# Summon beast is useless while you have a beast
# Bosses don't have enough health
# Special effects for each Boss, Special effects for you after defeating them
# How you kill? variety
# classes
# interactive manual
# Stabby-stabby legendary weapon, 1-2 dmg chance to oneshot, unlimited stabs
# CLasses - passive + 1 active per fight,
# Hunter - passive - sometimes beast attacks twice, active - trap
# warrior - passive - block, active - enrage take 3, 6, 9, 12 damage each time you attack but also do + 10/15/20 damage per attack
# priest - passive - heal, active - chainspells random spells until cancel, burst, stun, 

