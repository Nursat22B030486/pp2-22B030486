import os

for letter in range(65, 91):
    with open(f"{chr(letter)}.txt", 'x') as f:
        f.write(f'{chr(letter)}')