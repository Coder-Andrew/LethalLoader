import fresh_install
import update_mods

def display_menu():
    menu_options = {
        0: "Exit the program",
        1: "Fresh install mods (install BepinEx, LCapi, and BiggerLobbies)",
        2: "Update mods (updates LCapi and BiggerLobbies)"
    }
    for key in menu_options.keys():
        print(f"{key}: {menu_options[key]}")

def get_user_choice():
    while True:
        try:
            user_input = int(input("\nEnter your choice: "))
            if user_input in range(0, 3):
                return user_input
            else:
                print("Inavlid choice. Please Try again.")
        
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == '__main__':
    print("-------Welcome to Lethal Loader!-------\n")

    display_menu()
    choice = get_user_choice()

    if choice == 1:
        fresh_install.fresh_install_lc_mods()
        input("Install complete. Press enter...")
    elif choice == 2:
        update_mods.update_lc_mods()
        input("Update complete. Press enter...")