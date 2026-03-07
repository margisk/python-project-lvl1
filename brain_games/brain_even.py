from random import randint

import prompt

from brain_games.cli import welcome_user


def brain_even_game():
    user_name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    correct_answer_counter = 0
    correct_answers_to_win = 3

    while correct_answer_counter < correct_answers_to_win:
        number_to_ask = randint(1, 100)
        print(f'Question: {number_to_ask}')
        user_answer = ask_user()
        correct_answer = is_even_explicit(number_to_ask)
        if user_answer != correct_answer:
            print(f"'{user_answer}' is a wrong answer! " 
                  f"The correct answer was '{correct_answer}'.")
            print(f"Let's try again, {user_name}!")
            return
        print('Correct!')
        correct_answer_counter += 1
    print(f'Congratulations, {user_name}!')


def ask_user():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def is_even_explicit(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'
