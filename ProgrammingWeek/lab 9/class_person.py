class person:
    def __init__(self,name,address,weight,height):
        self.name = name
        self.address = address
        self.weight = float(weight)
        self.height = float(height)

    def show(self):
        
        return f"ชื่อ {self.name} ที่อยู่ {self.address} น้ำหนัก {self.weight} ส่วนสูง {self.height}"

    def getBMI(self):
        bmi = self.weight/((self.height*0.01)**2)
        if bmi < 18.5:
            health = "underweight"
        if 18.5 < bmi < 22.9:
            health = "normal weight"
        if 23.0 < bmi:
            health = "underweight"
    
        
        return f"bmi: {health}"

class student(person):
    def __init__(self,name,address,weight,height,student_id,course,gpa):
            super().__init__(name,address,weight,height)
            self.student_id = student_id
            self.course = course
            self.gpa = float(gpa)

    def show(self):
            show_info_student = super().show()
            return f"{show_info_student} รหัสประจำตัวนักเรียน {self.student_id} วิชา {self.course} gpa {self.gpa}"
    
class employee(person):
    def __init__(self,name,address,weight,height,employee_id,department,salary):
            super().__init__(name,address,weight,height)
            self.employee_id = employee_id
            self.department = department
            self.salary = float(salary)

    def show(self):
            show_info_employee = super().show()
            return f"{show_info_employee} รหัสประจำตัวพนักงาน {self.employee_id} แผนก {self.department} เงินเดือน {self.salary}"   
    

person1 = person("bt","taopoon","42","162")
student1 = student("bt","taopoon","42","162","43369","Maths","3.75")
employee1 = employee("bt","taopoon","42","162","43369","finance","35000")

print(person1.show())
print(person1.getBMI())
print(student1.show())
print(student1.getBMI())
print(employee1.show())
print(employee1.getBMI())