class Question:
    def __init__(self,question,options,correct_answer):
        self.question = question
        self.options = options
        self.correct_answer = correct_answer
    def check_answer(self, selected_option):
        return selected_option == correct_answer

class GameRound:
    def __init__(self,questions):
        self.questions = questions
        # set the index to 0
        self.current_question_index = 0
        
        # score to 0
        self.score = 0


    def get_current_question(self):
        return self.questions[self.question_index]

    def check_answer(self,selected_option):
        current_question = self.get_current_question()
        if current_question.check_answer(selected_option):
            self.score += 1
            
        self.current_question_index += 1
        
    def is_round_over(self):
        return self.current_question_index >= len(self.questions)


class Player:
    def __intit__(self,name):
        self.name = name
        self.score = 0

        


    
