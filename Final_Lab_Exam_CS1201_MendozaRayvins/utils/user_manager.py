import os
from utils.user import UserMixin

class UserManager(UserMixin):
    def __init__(self, username):
        self.username = username
        self.users = {}
        self.data_folder = "data"
        self.user_file = os.path.join(self.data_folder, "accounts.txt")
        self.user_date_file = os.path.join(self.data_folder, "user_date.txt")

        super().__init__(self.user_file)
        self.create_data_folder()

    def create_data_folder(self):
        if not os.path.exists(self.data_folder):
            os.makedirs(self.data_folder)

    def load_users(self):
        try:
            with open(self.user_file, "r") as file:
                for line in file:
                    username, password = line.strip().split(":")
                    self.user_accounts[username] = {"password": password}
        except FileNotFoundError:
            print("User accounts file not found.")
           
    def save_users(self, username, password):
        try:
            with open(self.user_file, "a") as file:
                file.write(f"{username}:{password}\n")
            print("User account saved successfully.")
        except Exception as e:
            print(f"Error saving user account: {e}")
    
    def validate_username(self, username):
        if len(username) < 4:
            print("Username must contain 4 characters long!!")
            return False
        return True
    
    def validate_password(self, password):
        if len(password) < 8:
            print("Password must contain 8 characters long!!")
            return False
        return True
    
    def register(self):
        username = input("Enter a username (at least 4 characters): ")
        password = input("Enter a password (at least 8 characters): ")
        
        if not self.validate_username(username) or not self.validate_password(password):
            return False
        
        if username in self.users:
            print("Username already exists!!")
            return False
        
        self.users[username] = password
        print('Sucessfully Registered')
        return True
    
    def log_in(self):
        while True:
            username = input("Enter a username (at least 4 characters): ")
            password = input("Enter a password (at least 8 characters): ")

            if username in self.users and self.users[username] == password:
                print("Log-In Sucessfully")
                return True
            else:
                print("Invalid username or password")
                return False
            break

