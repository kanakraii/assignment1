#calculate all elements in the list 
l1=[1,2,4,6,3,7]
print(l1)
l1sum=(sum(l1))
print("Sum of the list is:",l1sum)
#find the smallest number
l1.sort()
print("\nThe smallest number from the list is:",l1[0])
#find the largest number
print("\nThe largest number from the list is:",l1[-1])
#ascending order
l1.sort()
print("\nThe list in ascending order:",l1)
#descending order
l1.sort(reverse=True)
print("\nThe list in descending order:",l1)
#convert to tuple
t1=tuple(l1)
print("\nTuple:",t1)
#clear list
l1.clear()

