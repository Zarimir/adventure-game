import config

"""Defines Item characteristics"""
class Item():
    def __init__(self):
        self.category = ""
        self.kind = ""
        self.name = ""
        self.characteristics = {}

    def __str__(self):
        string = "Item:"
        string += "\ncategory: " + str(self.category)
        string += "\nkind: " + str(self.kind)
        string += "\nname: " + str(self.name)
        for characteristic in self.characteristics:
            string += "\n" + str(characteristic) + ":"
            for sub in self.characteristics[characteristic]:
                string += "\n\t- " + str(sub) + " : " + str(self.characteristics[characteristic][sub])
        return string
    
    def trigger(self, characteristic):
        if characteristic in self.characteristics and "effect" in self.characteristics[characteristic]:
            if characteristic == "equippable":
                return self.equip()
            if characteristic == "consumable":
                return self.consume()
            if characteristic == "usable":
                return self.use()
            if characteristic == "charming":
                return self.charm()
            
    def equip(self):
        if self.attr("equipped") and self.attr("durability"):
            return self.attr("equippable_effect")
        elif not self.attr("durability"):
            self.unset("equippable")

    def consume(self):
        if self.attr("quantity"):
            self.attr("quantity", self.attr("quantity") - 1)
            return self.attr("consumable_effect")
        else:
            self.unset("consumable")
        
    def use(self):
        if not self.attr("counter"):
            self.attr("counter", self.attr("cooldown"))
            return self.attr("usable_effect")
        else:
            self.attr("counter", self.attr("counter") - 1)

    def charm(self):
        return self.attr("charming_effect")

    def damage(self, damage):
        if self.attr("equipped"):
            self.attr("durability", self.attr("durability") - damage)
            if self.attr("durability") <= 0:
                self.unset("equippable")
    
    def attr(self, attribute, value=None):
        for characteristic in self.characteristics:
            if attribute in config.bijective_map[characteristic]:
                if attribute in config.normalized_map:
                    attribute = config.normalized_map[attribute]
                if value == None:
                    return self.characteristics[characteristic][attribute]
                else:
                    self.characteristics[characteristic][attribute] = value
        
    def set_equippable(self, position=None, durability=None, effect=None):
        equippable = {}
        equippable["equipped"] = False
        equippable["position"] = position
        equippable["durability"] = durability
        equippable["effect"] = effect
        self.characteristics["equippable"] = equippable

    def set_consumable(self, quantity=None, effect=None):
        consumable = {}
        consumable["quantity"] = quantity
        consumable["effect"] = effect
        self.characteristics["consumable"] = consumable

    def set_usable(self, cooldown=None, effect=None):
        usable = {}
        usable["cooldown"] = cooldown
        usable["counter"] = 0
        usable["effect"] = effect
        self.characteristics["usable"] = usable

    def set_charming(self, effect=None):
        charming = {}
        charming["effect"] = effect
        self.characteristics["charming"] = charming

    def unset(self, characteristic):
        self.characteristics.pop(characteristic, None)

    def filter_characteristics(self, characteristics="all", attribute=None, condition=None):
        if attribute == None:
            if type(characteristics) == list:
                for characteristic in characteristics:
                    if characteristic not in self.characteristics:
                        return None
                return self
            elif characteristics == "all":
                return self
            elif characteristics in self.characteristics:
                return self
            elif characteristics == None and not self.characteristics:
                return self
        else:
            if self.attr(attribute):
                if not condition or condition and condition(self.attr(attribute)):
                    return self

    def trigger_effects(self, characteristics=None):
        if type(characteristics) == list or characteristics == None:
            if characteristics == None:
                arg = self.characteristics
            else:
                arg = characteristics
            effects = []
            for characteristic in arg:
                effect = self.filter_effect(characteristic)
                if effect != None:
                    effects.append(effect)
            return effects
        return self.trigger(characteristics)
