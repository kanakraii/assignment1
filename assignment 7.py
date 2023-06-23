def fo(file="ex.txt"):
    try:
        f = open(file, "a+")
        print("~FILE OPENED~")
        roll_no = int(input("Enter rollno:"))
        name = input("Enter name:")
        div = input("Enter division:")
        f.writelines(str(roll_no))
        f.writelines(name)
        f.writelines(div)
        print("~DATA ENTERED~")

        f.seek(0)
        data= f.readline()
        print("~FILE DATA:~")
        print(data)
    except IOError:
        print("IOError exception handled")
    except ValueError:
        print("ValueError exception handled. Please enter a valid rollno.")
    except Exception:
        print("Exception handled")
    finally:
        print("This is the finally block")

  
    f.close()
    print("~FILE CLOSED~")
fo("ex.txt")
