from random import *
from string import ascii_letters as ascii

pw = ''
def pw_length():
    try:
        pw_len = int(input('password lenth: '))
    except SyntaxError:
        print('Syntax inncorect. Pleas provide an integer.')
        print()
        pw_length()

pw_length()

for i in range(pw_len):
    chr = choice(ascii)
    pw += chr

print(f'Your generated password: {pw} (_copy_)')