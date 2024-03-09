# 2a) Defined as a function F as Fn = Fn-1 + Fn-2. Write a Python program that accepts a value 
# for N (where N >0) as input and pass this value to the function. Display a suitable error 
# message if the condition for input value is not followed. 


def fn(n):
     if n == 1:
         return 0
     elif n == 2:
         return 1
     else:
         return fn(n-1) + fn(n-2)
num = int(input("Enter a number : "))
if num > 0:
 print("fn(", num, ") = ",fn(num) , sep ="")
else:
 print("Error in input")
