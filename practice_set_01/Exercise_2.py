# Exercise 2: Print the sum of the current number and the previous number

"""
    Write a program to iterate the first 10 numbers, and in each iteration, 
    print the sum of the current and previous number.
"""

prev_num = 0
for i in range(0, 11):
    sum = prev_num + i
    print("current no: ", i, "Previous No: ", prev_num, "sum = ", sum)
    prev_num = i
