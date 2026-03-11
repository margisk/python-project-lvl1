import prompt


def get_answer():
    user_answer = prompt.string('Your answer: ')
    return user_answer


def check_answer(user_answer, correct_answer):
    if user_answer != correct_answer:
        return False
    return True
