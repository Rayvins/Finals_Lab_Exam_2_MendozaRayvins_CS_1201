import os

class UserMixin:
    def __init__(self, user_file):
        self.user_file = user_file

    def show_user(self):
        try:
            with open(self.user_file, "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return None
        except ValueError:
            print("Error: Invalid data in score file.")
            return None
    
    def show_user_date(self):
        try:
            with open(self.user_file, "r") as file:
                return file.read()
        except FileNotFoundError:
            return None
  
    

