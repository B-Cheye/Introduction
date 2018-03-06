"Write a programme that tells a person his/her name and the year he/she will be 100 years old"
name = input('What is your name?')
age = int(input('How old are you?'))
year = str((2018 - age)+100)
print(name + ' ' + 'will be 100 years old in the year ' + year)
print('{} will be 100 years old in the year {} '.format(name, year))
