""" Exercise 7: Return the count of a given substring from a string
Write a program to find how many times substring “Emma” appears in the given string.        """


string = "Emma is good developer. Emma is a writer"
word = str(input("Enter a word tobe search "))
count = string.count(word)

if word in string:
    print(word, "appears", count, "times")
else:
    print("No Matches Found.. ")
