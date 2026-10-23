class Student:
    def __init__(self, student_id, name, course, age):
        self.student_id = student_id
        self.name = name
        self.course = course
        self.age = int(age)
       
    def show(self):
        print(f"รหัสประจำตัว {self.student_id} ชื่อ {self.name} รายวิชา {self.course} อายุ {self.age}")

def show_youngest_student(students):
    if not students:
        return

    youngest = students[0]

    for s in students:
        if s.age < youngest.age:
            youngest = s

    print("นักเรียนที่มีอายุน้อยที่สุดคือ:")
    youngest.show()

students_list = []

with open("class_student.txt", "r", encoding="utf-8") as file:
    for line in file:
        data = line.strip().split(",") 
        if len(data) == 4:
            s = Student(data[0], data[1], data[2], data[3])
            students_list.append(s)

show_youngest_student(students_list)