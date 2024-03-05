class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False


student1 = Student()
student1.name = "me"
student1.age = 18
print(student1.name)
print(student1.age)

# mixed_numbers = ["Hello", -34, "java", True]
# print("1", mixed_numbers[-1])
# mixed_numbers[1] = "Hi"
# print("2", mixed_numbers)
#
# mixed_tuple = (1, 2, 3, 4, 5)
# print("3", mixed_tuple)
