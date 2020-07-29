class Item():
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value

class Weapon(Item):
    def __init__(self, name, type, value, attack, speed, hands, status):
        super().__init__(name, type, value)
        self.attack = attack
        self.speed = speed
        self.hands = hands
        self.status = status

class Armor(Item):
    def __init__(self, name, type, value, health, armor, status):
        super().__init__(name, type, value)
        self.health = health
        self.armor = armor
        self.status = status

class Consumable(Item):
    def __init__(self, name, type, value, health):
        super().__init__(name, type, value)
        self.health = health