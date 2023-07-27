from moduleassign9 import MyOperations, FileOperationException

#file operations
file_operations = MyOperations("sample.txt")
try:
    file_operations.write_file("text file")
    content = file_operations.read_file()
    print("File content:", content)
except FileOperationException as e:
    print("File operation error:", e)

#mathematical operations
math_operations = MyOperations(None)
print("Addition:", math_operations.add(5, 10))
print("Subtraction:", math_operations.subtract(15, 8))

#string operations
try:
    result = math_operations.concatenate("hello, ", "user")
    print("Concatenated string:", result)

    
    invalid_result = math_operations.concatenate("Hello, ", 123)  
except ValueError as e:
    print("Invalid string operation:", e)
