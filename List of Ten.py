"""A programme that returns a list of elements that are less than the input number """
j = int(input('Enter the number'))
list0 = [1, 3, 4, 6, 7, 3, 5, 67, 9, 9, 45, 4, 5, 34, 3, 23, 6, 7, 8]
# list1 = []
# for num in list0:
#
#     if num < j:
#         list1.append(num)
new = [i for i in list0 if i < j]
print(new)
