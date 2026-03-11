from random import choice, randint

INSTRUCTION = "What is the result of the expression?"
OPERATIONS = ["+", "-", "*"]


def generate_qa_pair() -> tuple:
    operation = choice(OPERATIONS)
    numbers = (randint(1, 100), randint(1, 100))
    (first_num, second_num) = numbers
    question = f'{first_num} ' + operation + f' {second_num}'
    answer = 0
    match operation:
        case "+":
            answer = first_num + second_num
        case "-":
            answer = first_num - second_num
        case "*":
            answer = first_num * second_num
    return (question, str(answer))
