class FileOperationException(Exception):
    pass

class MyOperations:
    def __init__(self, filename):
        self.filename = filename

    def read_file(self):
        try:
            with open(self.filename, 'r') as file:
                content = file.read()
            return content
        except FileNotFoundError:
            raise FileOperationException(f"File '{self.filename}' not found.")
        except Exception as e:
            raise FileOperationException(f"Error reading file: {e}")

    def write_file(self, data):
        try:
            with open(self.filename, 'w') as file:
                file.write(data)
            return True
        except Exception as e:
            raise FileOperationException(f"Error writing to file: {e}")

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def concatenate(self, str1, str2):
        if not isinstance(str1, str) or not isinstance(str2, str):
            raise ValueError("Both inputs must be valid strings.")
        return str1 + str2
