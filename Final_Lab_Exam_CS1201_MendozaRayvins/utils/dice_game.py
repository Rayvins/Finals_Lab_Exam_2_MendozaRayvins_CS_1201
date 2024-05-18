import os
from utils.user_manager import UserManager
from utils.score import ScoreMixin
import random
from datetime import datetime

class DiceGame(ScoreMixin):
    
    def __init__(self, username):
        self.data_folder = "data"
        self.score_file = os.path.join(self.data_folder, "score.txt")
        self.score_date_file = os.path.join(self.data_folder, "score_date.txt")
        self.username = username

        super().__init__(self.score_file)
        self.create_data_folder()

    def create_data_folder(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def load_scores(self):
        if os.path.exists(self.score_file):
            with open(self.score_file, "r") as file:
                lines = file.readlines()
                if lines:
                    for line in lines:
                        score, username, date_str = line.strip().split(',')
                        date = datetime.strptime(date_str, '%Y-%m-%d %H:%M:%S')
                        print(f"Score: {score}, Username: {username}, Date: {date}")


    def save_scores(self, username):
        if self.score > 0:
            now = datetime.now()
            date_str = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            with open(self.score_file, "a") as file:
                file.write(f"{self.score},{username},{date_str}\n")

    def play_game(self):
        total_points = 0

        while True:
            user_points = 0

            for round_num in range(1, 4):
                print(f"\nRound {round_num}")
                dice1 = random.randint(1,6)
                dice2 = random.randint(1,6)
             
                print(f"You roled: {dice1}")
                print(f"CPU roled: {dice2}")
            
                if dice1 > dice2:
                    user_points += 1
                    total_points += 1
                    print(f"You won, you earned 1 point!!")
                elif dice1 < dice2:
                    print("CPU won")
                elif dice1 == dice2:
                    print("It's a tie!")
            
            print(f"Total points in this stage: {user_points}")
            print(f"Total points in this game: {total_points}")

            
            if user_points >= 2:
                print("You can proceed to the next stage")
                choice = input("Do you want to continue? (yes/no): ")
                if choice.lower() == 'no':
                    break
            else:
                print("You did not reach 2 points, better luck next time!")
                break
        if total_points > self.score:
            self.score = total_points
            self.save_scores(self.username)
    
    def show_top_scores(self):
        highest_score = self.show_top_scores()
        if highest_score is not None:
            print(f"Highest score: {highest_score}")
        else:
            print("No highest score recorded yet.")

    def logout():
        pass
    
    def menu(self):
        while True:
            print("Menu")
            print("1. Start Game")
            print("2. Show Top Score")
            print("3. Log-Out")
            choice = input("Enter your choice: ")
        
            if choice == '1':
                self.play_game()
            elif choice == '2':
                self.show_top_scores()
            elif choice == '3':
                print("Exiting the game!!")
                break
            else:
                print("Invalid choice. Please try again")

