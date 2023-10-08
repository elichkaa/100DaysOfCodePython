from question import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for entry in question_data:
    question_bank.append(Question(entry["question"], entry["correct_answer"]))

quiz = QuizBrain(question_bank)
while quiz.still_has_questions():
    quiz.next_question()

print("Quiz completed!")
print(f"You got {quiz.score}/{quiz.question_number} questions correctly.")