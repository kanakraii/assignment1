#break statement
print("*break statement*")
for i in range(1,11):
    if i==6:
        break
    print(i)
else:
    print("Loop exited")
#pass statement 
print("\n*pass statement*")
for i in range(1,11):
    if i==4:
        pass
    else:
        print(i)
#continue statement
print("\n*continue statement*")
for i in range(1,11):
    if i==5:
        continue
    else:
        print(i)
#for with else statement
print("\n*for with else statement*")
for i in range(1,11):
    if i%2==0:
        print("even number:",i)
    else:
        print("odd number:",i)
#while with else statement
print("\n*while with else*")
i=1
while i<=10:
    print(i)
    i+=4
else:
    print("loop exited")
