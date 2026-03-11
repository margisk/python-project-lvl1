from random import randint

INSTRUCTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def generate_qa_pair():
    question = randint(1, 100)
    answer = is_even_explicit(question)
    return (question, answer)


def is_even_explicit(number):
    if number % 2 == 0:
        return 'yes'
    return 'no'
