""""A programme that returns the divisors of a number"""
__author__ = 'BrianCheye'
x = range(2, 100)
num = int(input('Enter the number to check divisors'))
new = []
for a in x:
    if a % num == 0:
        new.append(a)
print(new)
