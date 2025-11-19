"""Arithmetic progression game."""
import random


DESCRIPTION = 'What number is missing in the progression?'
PROGRESSION_LENGTH = 10


def generate_progression(start, step, length):
    """Generate arithmetic progression."""
    progression = []
    for i in range(length):
        progression.append(start + i * step)
    return progression


def generate_question_and_answer():
    start = random.randint(1, 50)
    step = random.randint(2, 10)
    length = random.randint(5, PROGRESSION_LENGTH)
    
    progression = generate_progression(start, step, length)
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    
    progression[hidden_index] = '..'
    question = ' '.join(map(str, progression))
    
    return question, str(correct_answer)
