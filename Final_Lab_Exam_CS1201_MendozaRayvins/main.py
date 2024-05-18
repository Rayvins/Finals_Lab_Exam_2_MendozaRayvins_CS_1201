from utils.user_manager import UserManager
from utils.dice_game import DiceGame


def main():
    user_manager = UserManager('users')
    dice_game = DiceGame('user_manager')

    while True:
        print("\nWelcome to the Dice Roll Game!")
        print("\n1. Register")
        print("2. Log-In")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            user_manager.register()
        elif choice == '2':
            user_manager.log_in()
            dice_game.menu()
        elif choice == '3':
            print("Quitting the game!!")
            break
        else:
            print("")

if __name__=="__main__":
    main()