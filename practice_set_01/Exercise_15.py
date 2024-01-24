""" Exercise 15: 
    Write a function called exponent(base, exp) 
    that returns an int value of base raises to the power of exp.                                    """


base = int(input("Enter a Number: "))
exp = int(input("Enter it's Exponential Power: "))
msg = "Please Enter a Valid Exponential Power"


def exp_pow(base, exp):
    if exp >= 0:
        return base**exp
    else:
        return msg


print("Exponential Power is: ", exp_pow(base, exp))
