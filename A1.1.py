#Take two integer inputs from user a and b
#Define a complex variable a+bj
#Add a complex variable j to the previously defined complex variable
#Cast the final result as a string variable
#Print out the string result
print("Enter the value of a:")
a=int(input())
print("Enter the value of b:")
b=int(input())
print("a.", a)
print("b.", b)
complex0=complex(a,b)
c=complex0+1j
print(c)
string=c
c_string=str(c)
print("The result is:", c_string)