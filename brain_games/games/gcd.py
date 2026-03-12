from random import randint

INSTRUCTION = 'Find the greatest common divisor of given numbers.'


def generate_qa_pair() -> tuple:
	numbers = (randint(1, 100), randint(1, 100))
	(first_num, second_num) = numbers
	question = f'{first_num} ' + f'{second_num}'
	answer = calculate_gcd(first_num, second_num)
	return (question, str(answer))


def calculate_gcd(num1, num2):
	while num2 != 0:
		num1, num2 = num2, num1 % num2
	return num1