import string, random

letter_input1 = input("Choose a letter 'V' for vowels ,'C' for consonants,'L' for any letter")
letter_input2 = input("Choose a letter 'V' for vowels ,'C' for consonants,'L' for any letter")
letter_input3 = input("Choose a letter 'V' for vowels ,'C' for consonants,'L' for any letter")
letter_input4 = input("Choose a letter 'V' for vowels ,'C' for consonants,'L' for any letter")
letter_input5 = input("Choose a letter 'V' for vowels ,'C' for consonants,'L' for any letter")

Vowels = 'aeiouy'
Consonants = 'bcdfghjklmnpqrstvwxz'
Letter = string.ascii_lowercase


def baby_name_generator():
    if letter_input1 == 'v':
        letter1 = random.choice(Vowels)
    elif letter_input1 == 'c':
        letter1 = random.choice(Consonants)
    elif letter_input1 == 'l':
        letter1 = random.choice(Letter)
    else:
        letter1 = letter_input1

    if letter_input2 == 'v':
        letter2 = random.choice(Vowels)
    elif letter_input2 == 'c':
        letter2 = random.choice(Consonants)
    elif letter_input2 == 'l':
        letter2 = random.choice(Letter)
    else:
        letter2 = letter_input2

    if letter_input3 == 'v':
        letter3 = random.choice(Vowels)
    elif letter_input3 == 'c':
        letter3 = random.choice(Consonants)
    elif letter_input3 == 'l':
        letter3 = random.choice(Letter)
    else:
        letter3 = letter_input3

    if letter_input4 == 'v':
        letter4 = random.choice(Vowels)
    elif letter_input4 == 'c':
        letter4 = random.choice(Consonants)
    elif letter_input4 == 'l':
        letter4 = random.choice(Letter)
    else:
        letter4 = letter_input4

    if letter_input5 == 'v':
        letter5 = random.choice(Vowels)
    elif letter_input5 == 'c':
        letter5 = random.choice(Consonants)
    elif letter_input5 == 'l':
        letter5 = random.choice(Letter)
    else:
        letter5 = letter_input5

    generated_name = letter1+letter2+letter3+letter4+letter5

    return generated_name
for name in range(20):
    print(baby_name_generator())
