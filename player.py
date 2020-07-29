from screens import *
from utils import *
from items import *
import json
import random

class Player():
    def __init__(self):
        self.gold = 250
        self.inventory = []

    # character creation functions

    def character_creation(self):
        temp_name = ''
        while(temp_name == ''):
            temp_name = input('=== What is your name ? ===\n')
        self.name = temp_name
        cls()
        
        with open('classes.json') as json_file:
            classes_json = json.load(json_file)

        while True:
            cls()
            select_class_screen(self.name)

            try:
                choice = input()
                class_json = classes_json[choice]
            except:
                invalid_selection_message()
                continue

            self.class_name = class_json['name']
            self.class_description = class_json['description']

            print('| You choose the '+self.class_name+' |')
            print('| '+self.class_description+' |')
            yes_no_screen()
            choice2 = input('| Are you sure about your selection ? |\n')
            if (choice2 == '1'):
                break
            elif (choice2 == '2'):
                continue
            else:
                invalid_selection_message()

            cls()

        self.hp = class_json['hp']
        self.max_hp = class_json['max_hp']
        self.armor = class_json['armor']
        self.attack = class_json['base_attack']
        self.speed = float(class_json['base_speed'])
        self.equip_starting_gear(class_json['starting_gear'])
        cls()

    def equip_starting_gear(self, starting_gear):
        for item_types in starting_gear:
            if item_types == 'weapons':
                for item in starting_gear['weapons']:
                    self.inventory.append(
                        Weapon(
                            item, 
                            item_types, 
                            int(starting_gear['weapons'][item]['value']),
                            int(starting_gear['weapons'][item]['attack']),
                            float(starting_gear['weapons'][item]['speed']),
                            int(starting_gear['weapons'][item]['hands']),
                            (starting_gear['weapons'][item]['status'])
                            )
                        )

            if item_types == 'armors':
                for item in starting_gear['armors']:
                    self.inventory.append(
                        Armor(
                            item, 
                            item_types, 
                            int(starting_gear['armors'][item]['value']),
                            int(starting_gear['armors'][item]['health']),
                            int(starting_gear['armors'][item]['armor']),
                            (starting_gear['armors'][item]['status'])
                            )
                        )

            if item_types == 'consumables':
                for item in starting_gear['consumables']:
                    self.inventory.append(
                        Consumable(
                            item, 
                            item_types, 
                            int(starting_gear['consumables'][item]['value']),
                            int(starting_gear['consumables'][item]['health']),
                            )
                        )

        self.recalculate_gear()

    # helping character stats functions

    def show_stats(self):
        print('''
            === {name} - {class_name} ===
            === GOLD : {gold} ===
            === HP : {hp}/{max_hp} ===
            === ARMOR : {armor} ===
            === DMG\\ATTACK : {dmg_attack} ===
        '''.format(name=self.name, 
            class_name=self.class_name, 
            gold=self.gold, 
            hp = self.hp,
            max_hp=self.max_hp+self.armor_health, 
            armor=self.armor+self.armor_armor, 
            dmg_attack=(self.attack*self.speed)+self.weapon_dpa)
        )

    def recalculate_gear(self):
        self.weapon_dpa = 0
        self.armor_armor = 0
        self.armor_health = 0
        self.free_hands = 2
        for items in self.inventory:
            if items.type == 'weapons':
                if items.status == 'equipped':
                    self.weapon_dpa += (items.attack * items.speed)
                    self.free_hands -= items.hands
            elif items.type == 'armors':
                if items.status == 'equipped':
                    self.armor_armor += items.armor
                    self.armor_health += items.health

        if self.hp > self.max_hp:
            self.hp = self.max_hp + self.armor_health

    # inventory management functions

    def show_inventory(self):
        print('~~~ INVENTORY ~~~')
        print('~~~ EQUIPPED ~~~')
        for item in self.inventory:
            try:
                if item.status == 'equipped':
                    if (item.type == 'weapons'):
                        print( 
                            str(self.inventory.index(item)+1) + ' - ' + 
                            item.name + ' --- ' + 
                            item.type + ' --- ' + 
                            str(item.value) +' gold --- ' + 
                            str(item.attack) + ' damage --- speed: ' + 
                            str(item.speed) + ' --- weapon uses ' + 
                            str(item.hands) +' hand(s) --- ' +
                            (item.status)
                        )
                    if (item.type == 'armors'):
                        print( 
                            str(self.inventory.index(item)+1) + ' - ' + 
                            item.name + ' --- ' + 
                            item.type + ' --- ' + 
                            str(item.value) +' gold --- ' + 
                            str(item.health) + ' HP --- ' + 
                            str(item.armor) + ' ARMOR --- ' + 
                            (item.status)
                        )

            except:
                continue

        print('~~~ GEAR ~~~')
        for item in self.inventory:
            try:
                if item.status == 'unequipped':
                    if (item.type == 'weapons'):
                        print( 
                            str(self.inventory.index(item)+1) + ' - ' + 
                            item.name + ' --- ' + 
                            item.type + ' --- ' + 
                            str(item.value) +' gold --- ' + 
                            str(item.attack) + ' damage --- speed: ' + 
                            str(item.speed) + ' --- weapon uses ' + 
                            str(item.hands) +' hand(s) --- ' +
                            (item.status)
                        )
                    if (item.type == 'armors'):
                        print( 
                            str(self.inventory.index(item)+1) + ' - ' + 
                            item.name + ' --- ' + 
                            item.type + ' --- ' + 
                            str(item.value) +' gold --- ' + 
                            str(item.health) + ' HP --- ' + 
                            str(item.armor) + ' ARMOR --- ' + 
                            (item.status)
                        )
            except:
                continue

        print('~~~ CONSUMABLES ~~~')
        for item in self.inventory:
            if item.type == 'consumables':
                    print( 
                    str(self.inventory.index(item)+1) + ' - ' + 
                    item.name + ' --- ' + 
                    item.type + ' --- ' + 
                    str(item.value) +' gold --- grants ' + 
                    str(item.health) + ' HP on use'
                    )
            
        print('~~~~~~~~~~~~~~~~~')

    def check_item_conflict(self, item):
        if item.type == 'weapons':
            if self.free_hands >= item.hands:
                item.status = 'equipped'
            else:
                print('===     No free hands to equip weapon     ===')
                print('===        To equip another weapon        ===')
                print('===     please unequip the current one    ===')
                press_any_key()

        elif item.type == 'armors':
            for items in self.inventory:
                if items.type == 'armors' and items.status == 'equipped':
                    print('===     Armor already equipped     ===')
                    print('===     To equip another armor     ===')
                    print('=== please unequip the current one ===')
                    press_any_key()
                    return
            
            item.status = 'equipped'

    def free_item_slot(self, item):
        if item.type == 'weapons':
            self.free_hands += item.hands
        item.status = 'unequipped'

    def modify_gear(self, action, gear_index):
        gear_index = gear_index-1
        item = self.inventory[gear_index]
        if action == 'equip':
            self.check_item_conflict(item)
        elif action == 'unequip':
            self.free_item_slot(item)
            item.status = 'unequipped'
        self.recalculate_gear()

    def use_consumable(self, gear_index):
        gear_index = gear_index-1
        item = self.inventory[gear_index]
        if item.type == 'consumables':
            if self.hp == self.max_hp+self.armor_health:
                print('=== HEALTH ALREADY FULL ===')
                press_any_key()
                return
            self.hp += item.health
            if self.hp > self.max_hp:
                self.hp = self.max_hp + self.armor_health
                print('=== HEALTH POTION USED ===')
                del self.inventory[gear_index]

    def manage_inventory(self):
        while True:
            cls()
            self.show_stats()
            self.show_inventory()
            inventory_management_screen()

            choice = input('Choose what to do: ')
            choice_list = choice.split(' ')

            if (choice_list[0] == 'equip' or choice_list[0] == 'unequip'):
                self.modify_gear(choice_list[0], int(choice_list[1]))
                continue
            elif (choice_list[0] == 'use'):
                self.use_consumable(int(choice_list[1]))
                continue
            elif (choice_list[0] == 'x'):
                break
            else:
                invalid_selection_message()
                continue

    # shop management functions

    def generate_shop_stock(self):
        self.shop_stock = []

        with open('items.json') as json_file:
            items_json = json.load(json_file)

        for item_type in items_json:
            for item in items_json[item_type]:
                chance = random.randint(0,1)
                if chance:
                    if item_type == 'weapons':
                        self.shop_stock.append(
                            Weapon(
                                item, 
                                item_type, 
                                int(items_json[item_type][item]['value']),
                                int(items_json[item_type][item]['attack']),
                                float(items_json[item_type][item]['speed']),
                                int(items_json[item_type][item]['hands']),
                                (items_json[item_type][item]['status'])
                            )
                        )
                    
                    if item_type == 'armors':
                        self.shop_stock.append(
                            Armor(
                                item, 
                                item_type, 
                                int(items_json[item_type][item]['value']),
                                int(items_json[item_type][item]['health']),
                                int(items_json[item_type][item]['armor']),
                                (items_json[item_type][item]['status'])
                            )
                        )

                    if item_type == 'consumables':
                        self.shop_stock.append(
                            Consumable(
                                item, 
                                item_type, 
                                int(items_json[item_type][item]['value']),
                                int(items_json[item_type][item]['health'])
                            )
                        )

    def show_shop_stock(self):
        print('~~~ SHOP STOCK ~~~')
        for item in self.shop_stock:
            if item.type == 'weapons':
                print( 
                    str(self.shop_stock.index(item)+1) + ' - ' + 
                    item.name + ' --- ' + 
                    item.type + ' --- ' + 
                    str(item.value) +' gold --- ' + 
                    str(item.attack) + ' damage --- speed: ' + 
                    str(item.speed) + ' --- weapon uses ' + 
                    str(item.hands) +' hand(s)'  
                    )
            if item.type == 'armors':
                print( 
                    str(self.shop_stock.index(item)+1) + ' - ' + 
                    item.name + ' --- ' + 
                    item.type + ' --- ' + 
                    str(item.value) +' gold --- ' + 
                    str(item.health) + ' HP --- ' + 
                    str(item.armor) + ' ARMOR' 
                    )
            if item.type == 'consumables':
                print( 
                    str(self.shop_stock.index(item)+1) + ' - ' + 
                    item.name + ' --- ' + 
                    item.type + ' --- ' + 
                    str(item.value) +' gold --- grants ' + 
                    str(item.health) + ' HP on use'
                    )

    def do_trade(self, action, gear_index):
        gear_index = gear_index-1
        if (action == 'buy'):
            item = self.shop_stock[gear_index]
            if item.type == 'weapons':
                self.inventory.append(Weapon(item.name, item.type, item.value, item.attack, item.speed, item.hands, item.status))
            elif item.type == 'armors':
                self.inventory.append(Armor(item.name, item.type, item.value, item.health, item.armor, item.status))
            elif item.type == 'consumables':
                self.inventory.append(Consumable(item.name, item.type, item.value, item.health))
            self.gold -= item.value
            del self.shop_stock[gear_index]
        elif (action == 'sell'):
            item = self.inventory[gear_index]
            if item.type == 'weapons':
                self.shop_stock.append(Weapon(item.name, item.type, item.value, item.attack, item.speed, item.hands, item.status))
            elif item.type == 'armors':
                self.shop_stock.append(Armor(item.name, item.type, item.value, item.health, item.armor, item.status))
            elif item.type == 'consumables':
                self.shop_stock.append(Consumable(item.name, item.type, item.value, item.health))
            self.gold += item.value
            del self.inventory[gear_index]

        self.recalculate_gear()

    def shop(self):
        self.generate_shop_stock()
        while True:
            cls()
            self.show_stats()
            self.show_inventory()
            self.show_shop_stock()
            shop_screen()

            choice = input('Choose what to do: ')
            choice_list = choice.split(' ')

            if (choice_list[0] == 'buy' or choice_list[0] == 'sell'):
                self.do_trade(choice_list[0], int(choice_list[1]))
                print('=== Aaah, a fine choice ! ===')
                continue
            elif (choice_list[0] == 'x'):
                break
            else:
                invalid_selection_message()
                continue



    def home(self):
        pass

    def king(self):
        pass

    def save_game(self):
        pass
