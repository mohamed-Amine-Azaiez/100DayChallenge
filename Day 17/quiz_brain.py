class QuizBrain:
    def __init__(self,question_list):
        self.question_number=0
        self.question_list = question_list
        self.score=0
    
    def next_question(self):
        res=input(f"Q.{self.question_number+1}: {self.question_list[self.question_number].text} (True/False)?: ").lower()
        self.check_answer(res)
        

    def still_has_question(self):
        if len(self.question_list) < (self.question_number+1):
            print(f"You've completed The quiz.\nYour final score was {self.score}/{self.question_number}")
            return False
        else:
            return True
    def check_answer(self,res):
        if res == (self.question_list[self.question_number].answer).lower():
            print("You got it right!")
            self.score+=1
            print(f"Your current Score is {self.score}/{self.question_number+1}.")
        else:
            print("That's wrong.")
            print(f"The correct answer was: {self.question_list[self.question_number].answer}.")
            print(f"Your current Score is {self.score}/{self.question_number+1}.")
        self.question_number+=1
        print(self.question_number)
        print("\n")