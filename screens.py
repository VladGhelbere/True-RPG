from utils import *

def welcome_screen():
    print('''
    ==================================
    |     Welcome to True RPG !      |
    | This game was made by Vlad G.  |
    |      It's sort of an RPG.      |
    |            Enjoy !             |
    ==================================
    ''')
    press_any_key()

def goodbye_screen():
    print('''
    ==================================
    | Sorry to see you go so soon !  |
    |   Hope you enjoyed the game.   |
    |         Exiting now...         |
    ==================================
    ''')
    press_any_key()
    exit()

def menu_screen():
    print('''
    ==================
    |    MAIN MENU   |
    | 1 - START GAME |
    | 2 - LOAD GAME  |
    | 3 - EXIT GAME  |
    ==================
    |Select an option|
    '''
    )

def invalid_selection_message():
    print('''
    =============================================
    |      !!!   INVALID SELECTION   !!!        |
    | PLEASE READ THE OPTIONS AND CHOOSE AGAIN  |
    =============================================
    '''
    )
    press_any_key()

def select_class_screen(character_name):
    print('=== And what do you do for a living, '+character_name+' ? ===')
    print('''
    =================
    | 1 - SWORDSMAN |
    | 2 - HUNTER    |
    | 3 - ALCHEMIST |
    | 4 - ASSASIN   |
    | 5 - FARMER    |
    =================
    ''')

def yes_no_screen():
    print('''
        ===========
        | 1 - YES |
        | 2 - NO  |
        ===========
        ''')

def intro_screen():
    print('''
    =====================================================
    | You are a resident of the Unnamed City            |
    | Your father died before paying the king his debt  |
    | You as his son, have to repay him every coin      |
    | Today, you have been granted a hearing with him   |
    =====================================================
    ''')

def finish_intro_screen(character_class):
    print('=== Aaah, a mighty '+character_class+' huh ? ===')
    print('=== You should be able to repay your father\'s debt in no time ===')
    print('=== Do so, and you may still keep that piece of land he had ===')
    print('=== Maybe you\'ll even repair that old house of yours, but, debt first ===')
    
    print('''
    =================================================================
    |                     Your hearing is over.                     |
    | Exiting the gates of the keep, you think about your next move |
    |        You are now free to explore the city and wilds         |
    |           to earn enough money to repay your debt             |
    |              and maybe even rebuild your house                |
    =================================================================
    ''')

    press_any_key()

def controls_screen():
    print('''
    ========================================
    |               CONTROLS               |
    | 1,2,3... - Do action shown on screen |
    | I - Open Inventory (out of combat)   |
    | S - Save Game (only in city)         |
    ========================================
    | Tip: You should check your inventory |
    | after you enter the city to check on |
    |    the equipment you spawned with    |
    ========================================
    ''')

    press_any_key()

def city_menu_screen():
    print('''
    =========================================
    |           YOU ARE IN TOWN             |
    =========================================
    |      WHAT WOULD YOU LIKE TO DO ?      |
    | 1 - Go home                           |
    | 2 - Go to the shop                    |
    | 3 - Visit the king                    |
    | 4 - Fight into the arena              |
    | 5 - Start adventure                   |
    | I - Open Inventory                    |
    | S - Save Game                         |
    =========================================
    ''')

def inventory_management_screen():
    print('''
    =========================================
    |      WHAT WOULD YOU LIKE TO DO ?      |
    | equip - (item number)                 |
    | unequip - (item number)               |
    | use - (consumable number)             |
    | x - go back                           |
    =========================================
    ''')

def shop_screen():
    print('''
    =========================================
    |    WELCOME TO MY SHOP, TRAVELLER  !   |
    =========================================
    |      WHAT WOULD YOU LIKE TO DO ?      |
    | buy - (item number)                   |
    | sell - (item number)                  |
    | x - go back                           |
    =========================================
    ''')