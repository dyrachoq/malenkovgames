
import random
import math


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def generate_question_and_answer():
    
    num1 = random.randint(1, 100)
    num2 = random.randint(1, 100)
    
    question = f'{num1} {num2}'
    correct_answer = math.gcd(num1, num2)
    
    return question, str(correct_answer)
