""""Take two lists,
and write a program that returns a list that contains
only the elements that are common between the lists (without duplicates).
Make sure your program works on two lists of different sizes."""
import random
list1 = random.sample(range(1, 20), 6)
list2 = random.sample(range(1, 40), 10)
print(list1)
print(list2)


def dup(list01, list02):

    duplicate = []

    for i in list01:
        for j in list02:
            if i == j:
                duplicate.append(i)
                break
    print(duplicate)
dup(list1, list2)