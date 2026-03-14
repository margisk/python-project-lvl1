from math import ceil, sqrt
from random import randint

INSTRUCTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def generate_qa_pair() -> tuple:
    number = randint(1, 100)
    answer = check_if_prime_explicit(number)
    return (number, answer)


def check_if_prime_explicit(number):
    for divisor in range(2, ceil(sqrt(number))):
        if number % divisor == 0:
            return "no"
    else:
        return "yes"
