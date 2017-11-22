from random import randint
from inventory import Inventory
import selector

class Intelligence():
    def __init__(self):
        self.characters = []
        self.environment_cluster = []
        self.cluster = Cluster()

    def consume_clusters(self):
        for character in self.characters:
            self.normalize(character)
            self.cluster.consume(character.cluster)

    def normalize(self, character):
        for effect in character.cluster.effects:
            effect.subjects = [arg for subject in effect.subjects for arg in self.interpret_subject(character, subject)]
            
    def act(self, phase):
        for character in self.characters:
            character.act(phase)
            
    def interpret_subject(self, character, subject):
        if " + " in subject:
            return [real_subjects for subject in subject.split(" + ") for real_subjects in self.interpret_subject(character, subject)]
        elif " or " in subject:
            return [selector.pick_random([real_subjects for subject in subject.split(" or ") for real_subjects in self.interpret_subject(character, subject)])]
        else:
            if subject == "self":
                return [character]
            elif subject == "all":
                return self.characters
            elif subject == "allies":
                return self.get_allies(character)
            elif subject == "enemies":
                return self.get_enemies(character)
            elif subject == "random ally":
                return [selector.pick_random(self.get_allies(character))]
            elif subject == "random enemy":
                return [selector.pick_random(self.get_enemies(character))]

    def get_allies(self, character):
        return [someone for someone in self.characters if someone.party == character.party and someone != character]

    def get_enemies(self, character):
        return [someone for someone in self.characters if someone.party != character.party]
        
    def evaluate(self, phase):
        self.consume_clusters()
        self.normalize()
        self.clear()
        for effect in self.cluster.effects:
            effect.evaluate(phase)

class Character():
    def __init__(self, name):
        #self.game = game
        self.name = name
        self.health = 0
        self.attack = 0
        self.effects = []
        self.inventory = Inventory()
        self.party = 0
        self.cluster = Cluster()

    def __str__(self):
        return self.name
    
    def act(self, phase):
        self.inventory
        
    def collect_cluster(self):
        return self.cluster.collect()
    
    def loot(self, item):
        self.inventory.put(item)

    def target(self, effect):
        pass
            
    def evaluate(self, effect):
        if effect and effect.duration > 0:
            effect.duration -= 1
            if effect.command == "heal":
                self.heal(effect.value)
            if effect.command == "suffer":
                self.suffer(effect.value)

    def attack(self):
        pass

class Cluster():
    def __init__(self):
        self.effects = []

    def __str__(self):
        return str([str(effect) for effect in self.effects])

    def evaluate(self, phase):
        for effect in self.effects:
            effect.evaluate(phase)

    def push(self, effect):
        self.effects.append(effect)

    def pop(self):
        if self.effects:
            return self.effects.pop(len(self.effects) - 1)

    def normalize(self):
        self.effects = [effect for effect in self.effects if effect.duration > 0]
        
    def pop_all(self):
        self.effects, popped = [], self.effects
        return popped

    def push_all(self, effects):
        self.effects += effects

    def consume(self, cluster):
        self.push_all(cluster.pop_all())
        self.normalize()

class Effect():
    def __init__(self, name=False, subjects=False):
        self.name = name
        self.description = ""
        self.normalized = False
        self.min = ""
        self.max = ""
        self.duration = 5
        self.phases = []
        self.subjects = subjects

    def __str__(self):
        return ", ".join([str(subject) for subject in self.subjects])

    def construct_command(self, command):
        [command, [value, duration, phase, subject]]
        self.commands.append
    def extend(self, aspect):
        self.aspects.append(aspect)
        self.commands.append([command])
        
        

    def evaluate(self, phase):
        if self.normalized:
            if phase == self.phase:
                self.duration -= 1
                self.subject.evaluate(self.command, self.value)
        else:
            raise ValueError("Effect cannot be evaluated if it's not normalized")
        
class Player(Character):
    def __init__(self, name):
        super().__init__(name)
        self.specialization = False
        self.equipment = {}
        self.level = 1

    #def look()
                
    def specialize(self, specialization):
        if specialization == "warrior":
            self.__class__ = Warrior
            self.__init__()
        elif specialization == "hunter":
            self.__class__ = Hunter
            self.__init__()
        elif specialization == "priest":
            self.__class__ = Priest
            self.__init__()

    def loot(self):
        loot = self.game.get_loot()

class Mob():
    def __init__(self):
        self.level = 0

    @staticmethod
    def intiialize():
        
        return mob

class Game():
    def __init__(self):
        self.intelligence = Intelligence()
        self.environment = Environment()
        
    def initialize(self):
        self.player = Player()
        self.player.initialize()
        
    def encounter(self):
        self.environment.initialize()
        self.mob.initialize()
        while True():
            prepare()
            attack()
            evaluate() # break

    def prepare(self):
        self.calculate_effects()
        self.intelligence.act("prepare")

    def attack(self):
        self.intelligence.act("attack")
        pass

    def evaluate(self):
        self.intelligence.act("evaluate")
        pass

    def play(self):
        initialize()
        encounter()


a = Effect("a", ["self + self + self + random enemy + random enemy + random enemy or self"])
b = Effect("b", ["allies"])
c = Effect("c", ["self"])
d = Effect("d", ["enemies"])
e = Effect("e", ["all"])
f = Effect("f", ["random enemy"])
g = Effect("g", ["random ally"])
player = Player("Me")
ally = Player("ally")
ally.party = player.party
enemy = Player("You")
enemy.party = 15
third_person = Player("Other")
third_person.party = 131023
enemy_ally = Player("Enemy Ally")
enemy_ally.party = enemy.party
intelligence = Intelligence()
intelligence.characters = [player, enemy, ally, third_person]
effects = [a,b,c,d,e,f,g]
player.cluster.push_all(effects)
intelligence.consume_clusters()
for effect in effects:
    print(effect)
#intelligence.characters = ['1', '2', '3']
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
# Custom messages for types of weapons and for legendaries
