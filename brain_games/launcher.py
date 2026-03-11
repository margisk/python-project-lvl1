from brain_games.cli import welcome_user
from brain_games.util import get_answer

NUMBER_OF_ROUNDS = 3


def launch_game(game):
    user_name = welcome_user()
    print(game.INSTRUCTION)

    correct_answer_counter = 0
    while correct_answer_counter < NUMBER_OF_ROUNDS:
        question, correct_answer = game.generate_qa_pair()
        print(f'Question: {question}')
        user_answer = get_answer()
        if user_answer != correct_answer:
            print(f"'{user_answer}' is a wrong answer! " 
                  f"The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')
        correct_answer_counter += 1
    print(f'Congratulations, {user_name}!')
