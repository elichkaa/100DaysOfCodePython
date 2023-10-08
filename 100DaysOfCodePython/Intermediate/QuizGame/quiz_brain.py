class QuizBrain:
    def __init__(self, questions):
        self.question_number = 0
        self.questions = questions
        self.score = 0

    def next_question(self):
        current_question = self.questions[self.question_number]
        self.question_number += 1
        ans = input(f"Q{self.question_number}: {current_question.text}: ")
        self.check_answer(ans, current_question.answer)

    def still_has_questions(self):
        return self.question_number < len(self.questions)

    def check_answer(self, user_answer, correct_answer):
        if user_answer == correct_answer:
            print("You got it right! ")
            self.score += 1
        else:
            print("Wrong!")
        print(f"The correct answer is {correct_answer}")
        print(f"Current score: {self.score}/{self.question_number}\n")
