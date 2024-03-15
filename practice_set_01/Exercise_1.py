#   Exercise 1: Calculate the multiplication and sum of two numbers
"""    
   Q. Given two integer numbers, return their product only if 
      the product is equal to or less than 1000. 
      Otherwise, return their sum.                                                      """
                                                                                

# num1 = int(input("Enter first number : "))
# num2 = int(input("Enter second number : "))
 
def return_prod_sum(num1,num2):
    prod = num1 * num2
    sum = num1 + num2
    if prod <= 1000:
        return  prod
    else:
        return sum

result = return_prod_sum(150,200)
print(f"result is {result}")