# Exercise 4: Remove first n characters from a string

"""
    Write a program to remove characters from a string starting from zero up to n and return a new string.

    For example:
    remove_chars("pynative", 4) so output must be tive. Here, we need to remove the first four characters from a string.                                            """


def remove_char(word, n):
    x = word[n:]
    print("Original Word : ", word, "\n" "After removing chars : ", x, "\n")
    return x


remove_char("Hello world..!", 2)

remove_char(str(input("Enter a Word: ")), int(input("Enter no of word tobe remove: ")))
