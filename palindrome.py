""""Ask a user for a string and check whether it is a palindrome"""
word = input('Give me a word \n')
print(word)
print(word[::-1])
if word[:] == word[::-1]:
    print('{} is a palindrome'.format(word))
else:
    print('{} is Not a palindrome'.format(word))
