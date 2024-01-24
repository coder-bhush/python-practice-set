# No. is palindrome or not
n = int(input("Enter a Number: "))


def is_palindrome(n):
    str_n = str(n)
    rev_str = str_n[::-1]
    if str_n == rev_str:
        ans = "Given Number is Palindrome"
    else:
        ans = "Given Number is not Palindrome"
    return ans


print(is_palindrome(n))
