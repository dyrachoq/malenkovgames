import random
import prompt

def check(number):
	return number % 2 == 0

def main():
	wins_round = 3
	corr_answers = 0
	print('Welcome to the VD-games!')
	name = prompt.string('May I have your name?')
	print(f'Hello, {name}!')
	print('Answer "yes" if the number is even, otherwise answer "no".')
	while corr_answers < wins_round:
		number = random.randint(1,100)
		print(f'Question: {number}')
		answer = prompt.string('Your answer: ')
		
		if check(number):
			corr_answer = 'yes'
		else:
			corr_answer = 'no'

		if answer == corr_answer:
			print('Correct!')
			corr_answers += 1
		else:
			print(f'"{answer}" is wrong answer.')
			print(f"Let's try again, {name}!")
			return
	print(f'Congratulations, {name}!')

if __name__ == "__main__":
	main()
