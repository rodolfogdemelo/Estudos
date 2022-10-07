#Other Way to run the codecademy.py Script

import random

name = ''
question = ''
rdNb = random.randint(1, 9)
answers = ['Yes - definitely.',
           'It is decidedly so.',
           'Without a doubt.',
           'Reply hazy, try again.',
           'Ask again later.',
           'Better not tell you now.',
           'My sources say no.',
           'Outlook not so good.',
           'Very doubtful.']

if name == '':

    name = input('Whats Your Name?')
    question = input('Whats Your Question?')
    print(f'{name} askes: {question}')
    print(f'Answer: {answers[rdNb]}')

else:
    print('Error')
