#You are given a string.a = "GNIRTS-A-SI-SIHT"

#Perform the following operations:

#Reverse the string and store its value in variable b
#Split the resulting string b on - hyphen delimiter and store its value in variable c
#Join the strings of c using " " (space) snd store its value in variable d
#Print out the result in lower case
a="GNIRTS-A-SI-SIHT"
b=a[::-1]
print(b)
c=b.split("-")
print(c)
d=" ".join(c)
print(d)
result=d.lower()
print(result)