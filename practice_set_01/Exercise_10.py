# Exercise 10: Create a new list from two list using the following condition
"""
    Given two list of numbers, write a program to create a new list such that the new list should contain odd numbers from the first list and even numbers from the second list.                   """


list1 = [10, 20, 25, 30, 35]
list2 = [40, 45, 60, 75, 90]


print("List 1 : ", list1)
print("List 2 : ", list2)


def my_list(list1, list2):
    res_lst = list()
    for i in list1:
        if i % 2 != 0:
            res_lst.append(i)

    for i in list2:
        if i % 2 == 0:
            res_lst.append(i)

    res_lst.sort()
    return res_lst


print("result list : ", my_list(list1, list2))
