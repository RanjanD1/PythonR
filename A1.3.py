#Take two integer inputs from user a and b
#Define a variables which stores the result of integer division and float division of these two numbers
#Check if these two variables are equal. Return boolean result ie. True or False
#Print the results of these variables
print("Enter integers a and b:")
a=int(input())
b=int(input())
print("a.", a)
print("b.", b)
integer_division=a//b
float_division=a/b
e=integer_division==float_division
print("Integer division result:", integer_division)
print("Float division result:", float_division)
print("Equal?", e)