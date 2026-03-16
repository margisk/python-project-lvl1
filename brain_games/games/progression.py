from random import randint

INSTRUCTION = 'What number is missing in the progression?'


def generate_qa_pair() -> tuple:
	progression = generate_arithmetic_progression()
	position_to_hide = randint(1, len(progression) - 1)
	answer = progression[position_to_hide]
	progression[position_to_hide] = '..'
	return (' '.join(progression), str(answer))


def generate_arithmetic_progression() -> list:
	start = randint(1, 100)
	length = randint(5, 10)
	step = randint(1, 10)
	items = [str(start)]
	for i in range(1, length):
		curr_item = start + i * step
		items.append(str(curr_item))
	return items