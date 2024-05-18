import os

class ScoreMixin:
    def __init__(self, score_file):
        self.score_file = score_file
        self.score = 0
        self.load_scores = 0
    
    def show_score(self):
        try:
            with open(self.score_file, "r") as file:
                return int(file.read())
        except FileNotFoundError:
            return None
        except ValueError:
            print("Error: Invalid data in score file.")
            return None
    
    def show_score_date(self, score_file):
        try:
            with open(score_file, "r") as file:
                return file.read()
        except FileNotFoundError:
            return None