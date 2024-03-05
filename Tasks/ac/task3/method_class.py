class MyClass:
    def __init__(self):
        self.myString = ""

    def get_String(self):
        self.myString = input("my name is: ")

    def print_String(self):
        return self.myString.upper()

    def __repr__(self):
        return f'{self.get_String()}'




