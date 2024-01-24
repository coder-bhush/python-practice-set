#   Exercise 1: Calculate the multiplication and sum of two numbers
"""    
   Q. Given two integer numbers, return their product only if 
      the product is equal to or less than 1000. 
      Otherwise, return their sum.                                                      """
                                                                                

num1 = int(input("Enter first number : "))
num2 = int(input("Enter second number : "))
prod = num1 * num2

if prod <= 1000:
    print(prod)
else:
    print(num1 + num2)
