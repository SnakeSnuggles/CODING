import random


verb = ['jump', 'act','answer', 'approve', 'arrange', 'breax', 'build', 'buy', 'coach', ' colour', 'cough', 'create', 'complete', 'cry', 'dance', 'describe', 'draw', 'drink', 'eat', 'edit', 'enter', 'exit', 'imitate', 'invent', 'jump', 'laugh', 'lie', 'listen', 'paint', 'plan', 'play', 'read', 'replace', 'run', 'scream', 'see', 'shout', 'sing', 'skip', 'sleep', 'sneeze', 'solve', 'study', 'teach', 'touch', 'turn', 'walk', 'win', 'write', 'whistle', 'yank', 'zip']
verbchosen = verb[random.randint(0,len(verb))]
questions = [f'if you were to {verbchosen} how would you {verbchosen}.', f'If you were to choose to {verbchosen} why would you {verbchosen}?', f'If you were to {verbchosen} when would you {verbchosen}']
randq = random.randint(0, len(questions))
randv = random.randint(0,len(verb))

questionchosen = questions[randq]
print(questionchosen)

