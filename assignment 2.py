n1=int(input("Enter the first number:",))
n2=int(input("Enter the second number:"))
print("*Arithmetic operator*")
print("The floor division of ",n1,"and",n2,"is:",n1//n2)
print("The exponent of",n1,"and",n2,"is:",n1**n2)
print("*Assignment operator*")
n1+=1
print("+=",n1)
print("*Comparison operator*")
print("!=",n1!=n2)
print("*Logical operator*")
a=True
b=False
print("and",a and b)
print("*Bitwise operator*")
print("bitwise |",n1|n2)
print("*Identity operator*")
print("is ", n1 is n2)
print("*Membership operator*")
a='kanak'
print('k' in a)
print('n' is not a)