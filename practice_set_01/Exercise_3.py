# Print characters from a string that are present at an even index number

""" 
    Write a program to accept a string from the user and display characters that 
    are present at an even index number.

    For example, str = "pynative" so you should display 'p', 'n', 't', 'v'.
"""

string = str(input("Enter any word or string: "))
size = len(string)

for i in range(0, size - 1, 2):
    print(string[i])
