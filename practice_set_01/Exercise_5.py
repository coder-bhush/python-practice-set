# Exercise 5: Check if the first and last number of a list is the same

"""
    Write a function to return True if the first and last number of a given list is same. 
    If numbers are different then return False.                                              """


n = int(input("Enter a No. of Elements you have to enter: "))
print("Enter a Numbers: ")

# Get a list from user
n_list = list()

for i in range(0, n):
    nums = int(input())
    n_list.append(nums)
print("list : ",n_list)


def first_last_same(n_list):
    if n_list[0] == n_list[-1]:
        return True
    else:
        return False


print(first_last_same(n_list))
