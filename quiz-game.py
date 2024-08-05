# QUESTION CLASS

class Question:
    def __init__(self, text, answers, correct_index):
        self.text = text
        self.answers = answers
        self.correct_index = correct_index
    # class function - defined OUTSIDE of __init__ constructor:
    def display_answers(self):
        count = 0
        for a in self.answers:
            print(f"{count} {a}")
            count += 1

    # F-STRINGS are strings that allow us to include placeholder values of any data type:
    f_string_example = f"here is my placeholder:{10+10}"
    # print(f_string_example)


# return true or false based on if guess_index is correct
def display_result(question, guess_index):
    try:
        if int(guess_index) == int(question.correct_index):
            print('Correct')
            return True
        else:
            print (f"Sorry, the answer is {question.answers[question.correct_index]}")
            return False
    except:
        print('Enter an answer number please!')
        # Reruns question with new chance to input answer. Added true and false returns if keeping track of player score.
        return display_result(question, input())
    

    
test_question = Question('Which one is a color?', ['egg', 'garden', 'red'], 2)

# print(test_question.text)
# (test_question.display_answers())
    
# print(display_result(test_question, 2))

all_questions = [
    Question("How many legs does a cat have?", [10, 2, 1, 4, 3], 3),
    Question("How many number one singles does Mariah Carey have?", [9, 4, 3, 0, 10], 4),
    Question(
        "What year was the restaurant chain \"Steak 'n Shake\" founded in?",
        [1934, 1952, 1965, 1970],
        0
    )
]

# Run each question and take player input. Waits until input is given on current question before going to next question:
score = 0

for question in all_questions:
    print(question.text)
    question.display_answers()
    # Asks the user to input text. Returns what was entered as a string
    guess_input = input("What is your guess? ")

    if display_result(question, guess_input):
        score +=1

    # Print a blank line (visual effect)
    print()

print(f"Your score was {score} out of {len(all_questions)}")