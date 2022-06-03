class Student:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade # 0-100

    def get_grade(self):
        return self.grade


class Course:
    def __init__(self, name, max_students):
        self.name = name
        self.max_students = max_students
        self.students = []
        self.waiting_list = []

    def add_student(self, student):
        if len(self.students) < self.max_students:
            self.students.append(student)
            return True
        else:
            self.waiting_list.append(student)

    def get_average_grade(self):
        g = 0
        for i in self.students:
            g += i.get_grade()

        return g / len(self.students)




s1 = Student("tim", 42, 100)
s2 = Student("Lazy Davey", 33, 66)
s3 = Student("ronny", 18, 87)

course = Course("Physics 333",2)

course.add_student(s1)
course.add_student(s2)
course.add_student(s3)

#for i in course.students:
#    print(i.name)

print(course.get_average_grade())
#print(course.waiting_list[0].name)
