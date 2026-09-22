#Write a Python function that accepts two integer numbers. If the product of the two numbers is less than or equal to 1000, return their product; otherwise, return their sum.
num1=int(input('enter the 1st integer:'))
num2=int(input('enter the 2nd integer:'))
if num1*num2 <= 1000:
    print("Product of",num1,"And",num2,"is:",num1*num2)
else:
    print("Sum of",num1,"And",num2,"is:",num1+num2)