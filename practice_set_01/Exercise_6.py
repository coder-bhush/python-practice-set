# Exercise 6: Display numbers divisible by 5 from a list

"""    
    Iterate the given list of numbers and print only those numbers 
    which are divisible by 5.
"""


n = int(input("Enter a no. of elements in your list: "))
print("Enter elements into a list: ")

# To get list as a input from user..
lst = list()

for i in range(0, n):
    nums = int(input())
    lst.append(nums)


def num_div_by_5(lst):
    x = list()
    for i in lst:
        if i % 5 == 0:
            x.append(i)
    return x


print("numbers divisible by 5 in your list: ", num_div_by_5(lst))
