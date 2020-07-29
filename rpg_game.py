from screens import *
from player import *
from utils import *

def menu():
    welcome_screen()
    while True:
        menu_screen()
        choice = input('Make a selection: ')
        if (choice == '1'):
            break
        elif (choice == '2'):
            print('=== FEATURE NOT AVAILABLE YET ===')
            continue
        elif (choice == '3'):
            goodbye_screen()
        else:
            invalid_selection_message()
            continue
    cls()

def city_menu(player):
    while True:
        cls()
        player.show_stats()
        city_menu_screen()
        choice = input('Choose what to do: ')
        # go home
        if (choice == '1'):
            player.home()
            continue
        # go to the shop
        elif (choice == '2'):
            player.shop()
            continue
        # visit the king
        elif (choice == '3'):
            player.king()
            continue
        # fight into the arena
        elif (choice == '4'):
            print('=== FEATURE NOT AVAILABLE YET ===')
            continue
        # start adventure
        elif (choice == '5'):
            print('=== FEATURE NOT AVAILABLE YET ===')
            continue
        # open inventory
        elif (choice == 'i' or choice == 'I'):
            player.manage_inventory()
        # save character progress
        elif (choice == 's' or choice == 'S'):
            player.save_game()
        # invalid message
        else:
            invalid_selection_message()
            continue

def freemode(player):
    city_menu(player)

def game():
    intro_screen()
    press_any_key()
    player = Player()
    player.generate_shop_stock()
    player.character_creation()
    finish_intro_screen(player.class_name)
    controls_screen()
    freemode(player)



def main():
    cls()
    menu()
    game()



if __name__ == "__main__":
    main()