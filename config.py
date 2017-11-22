constructor = "constructor"

bijective_map = {}
bijective_map["equippable"] = ["equipped", "position", "durability", "equippable_effect"]
bijective_map["consumable"] = ["quantity", "consumable_effect"]
bijective_map["usable"] = ["cooldown", "counter", "usable_effect"]
bijective_map["charming"] = ["charming_effect"]
normalized_map = {}
normalized_map["equippable_effect"] = "effect"
normalized_map["consumable_effect"] = "effect"
normalized_map["usable_effect"] = "effect"
normalized_map["charming_effect"] = "effect"
item_characteristics = ["equippable", "consumable", "usable", "charming"]

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

common_weapon_chance = 7
epic_weapon_chance = 3
legendary_weapon_chance = 0
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
