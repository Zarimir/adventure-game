import config
import selector
import util
from item import Item

def generate_item(category):
    item = Item()
    item.category = category
    template = util.load_constructor()[category]
    location = template.pop("location")
    item.kind = selector.pick_random(template)
    template = template[item.kind]
    location += template["location"]
    names = util.read(location).split("\n")
    item.name = selector.pick_random(names)
    return item

def make_equippable(item):
    template = util.load_constructor()[item.category][item.kind]
    item.set_equippable()
    item.attr("position", selector.pick_random(template["positions"]))
    item.attr("durability", selector.pick_in_range(minimum=template["durability"]["min"], maximum=template["durability"]["max"]))
    set_effect(item, "equippable")
    

def make_consumable(item):
    template = util.load_constructor()[item.category][item.kind]
    item.set_consumable()
    item.attr("quantity", selector.pick_in_range(minimum=template["quantity"]["min"], maximum=template["quantity"]["max"]))
    set_effect(item, "consumable")

def make_usable(item):
    template = util.load_constructor()[item.category][item.kind]
    item.set_usable()
    item.attr("cooldown", selector.pick_in_range(minimum=template["cooldown"]["min"], maximum=template["cooldown"]["max"]))
    set_effect(item, "usable")

def make_charming(item):
    template = util.load_constructor()[item.category][item.kind]
    item.set_charming()
    set_effect(item, "charming")

def set_effect(item, category):
    effect = "NYI effect"
    item.characteristics[category]["effect"] = effect
       
def generate_weapon():
    weapon = generate_item("weapon")
    make_equippable(weapon)
    return weapon

def generate_armour():
    armour = generate_item("armour")
    make_equippable(armour)
    return armour

def generate_potion():
    potion = generate_item("potion")
    make_consumable(potion)
    return potion

def generate_artefact():
    artefact = generate_item("artefact")
    make_usable(artefact)
    return artefact

def gen(callback):
    for i in range(7):
        item = callback()
        print(item)
