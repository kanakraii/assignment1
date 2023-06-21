#defining function
def ds():
    roll_no=int(input("enter student rollno:"))
    name=input("enter student name:")
#datastruct- list
    l1=[roll_no,name]
    print("\nlist:",l1)
#data struct- dicitonary
    d1={"\nrollno":roll_no,"name":name}
    
    print("\ndict:",d1)
#data struct- set
    s1={roll_no,name}
    print("\nset:",s1)
#data struct- tuple
    t1=(roll_no,name)
    print("\ntuple:",t1)
#deleting
    print("\n")
    del l1
    del d1
    del s1
    del t1
#empty 
    print(l1)
    print(d1)
    print(s1)
    print(t1)
ds()