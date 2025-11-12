
import random


DESCRIPTION = 'What is the result of the expression?'


def generate_question_and_answer():
    
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    operators = ['+', '-', '*']
    operator = random.choice(operators)
    
    question = f'{num1} {operator} {num2}'
    
    if operator == '+':
        correct_answer = num1 + num2
    elif operator == '-':
        correct_answer = num1 - num2
    else:
        correct_answer = num1 * num2
    
    return question, str(correct_answer)
