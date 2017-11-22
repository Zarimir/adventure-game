import config
from item import Item

"""Represents the inventory of a character"""
class Inventory():
    def __init__(self):
        self.items = []

    def __str__(self):
        return "\n".join([str(item) for item in self.items])
    
    def fetch(self, name, index=1):
        items = [item for item in self.items if item.name == name]
        if type(index) == int and index >= 1 and len(items) >= index:
            return items[index - 1]
        
    def prnt(self):
        print("\n".join([item for item in self.items]))
        
    def collect_items(self, characteristics="all", attribute=None, condition=None):
        return [item for item in [item.filter_characteristics(characteristics, attribute, condition=condition) for item in self.items] if item != None]

    def trigger_effects(self, characteristic=None):
        effects = [effect for effect in [item.trigger_effects(characteristic) for item in self.items] if effect]
        if characteristic == None or type(characteristic) == list:
            effects = [effect for item_effects in effects for effect in item_effects]
        return effects

    def collect_usables(self):
        return self.collect_items("usable")

    def collect_consumables(self):
        return self.collect_items("consumable")

    def collect_charming(self):
        return self.collect_items("charming")

    def collect_equippable(self):
        return self.collect_items("equippable")

    """Collects all the items which are equipped"""
    def collect_equipped(self):
        return self.collect_items("equippable", "equipped", lambda equipped: equipped)
    
    """Collects all the items which cannot be used in any way"""
    def collect_useless(self):
        return self.collect_items(None)
        
    """Collects all the character positions which are equipped with an item"""
    def collect_equipped_positions(self):
        return [item.attr("position") for item in self.collect_equipped()]

    """Equips an item"""
    def equip(self, item):
        if item not in self.items:
            print("Cannot equip an item I don't own")
        elif item not in self.collect_equippable():
            print("This item cannot be equipped")
        elif item.attr("equipped"):
            print("This item is already equipped")
        elif not item.attr("position"):
            print("I do not know how to wear this item")
        elif item.attr("position") in self.collect_equipped_positions():
            print("I already wear something else")
        else:
            item.attr("equipped", value=True)

    """Unequips an equipped item"""
    def unequip(self, item):
        if item in self.collect_equipped():
            item.attr("equipped", value=False)
        else:
            print("Item was not being equipped")

    """Drops an item from the inventory; drops all useless items by default"""
    def drop(self, item=None):
        if item == None:
            for item in self.collect_useless():
                self.drop(item)
        elif item in self.items:
            self.items.remove(item)
            return item

    """Puts an item in the inventory"""
    def put(self, arg):
        if type(arg) == list:
            for item in arg:
                self.put(item)
        elif type(arg) == Item:
            if arg not in self.items:
                self.items.append(arg)
                arg.attr("equipped", False)
            else:
                print("Cannot put item " + str(arg) + " in the inventory, it is already in")
        else:
            print("Cannot put argument of type : " + str(type(arg)) + " in the inventory")

def prnt(items):
    for item in items:
        print(item)
invent = Inventory()
gen = Item("kind", "name")
axe = Item("axe", "Frostmourne")
axe.set_equippable("main-hand", 3)
sword = Item("sword", "Frostmourne")
sword.set_equippable("off-hand", 5, "block")
potion = Item("potion", "Health Potion")
potion.set_consumable(2, "heals you")
food = Item("food", "Pancake")
food.set_consumable(5, "heals you overtime")
totem = Item("totem", "Fire Totem")
totem.set_charming("burns enemies")
totem.set_equippable("off-hand", 10, "hit")
raw = [totem, sword, gen, axe, potion, food]
invent.put(raw)
invent.items[1].characteristics["equippable"]["equipped"] = True
invent.items[1].characteristics["equippable"]["position"] = "head"
