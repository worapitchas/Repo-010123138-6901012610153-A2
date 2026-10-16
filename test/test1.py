# โจทย์ข้อที่ 2: OOP และ Inheritance (การสืบทอดคลาส)
# เงื่อนไข: การสร้าง Class, Constructor, Attributes, Methods, Subclass และ Method Overriding
# โจทย์:จงสร้างคลาสแม่ Shape มี Attribute ชื่อ color และ Method area() 
# ที่คืนค่า 0 จงสร้างคลาสลูก Circle ที่สืบทอดจาก Shape มี Attribute เพิ่มเติมคือ radius 
# และทำการ Override Method area() เพื่อคำนวณพื้นที่วงกลม ($\pi \times r^2$)


class shape:
    def __init__(self,color):
        self.color = color

    def area(self):
        return 0

class circle(shape):
    def __init__(self,color,radius):
        super().__init__(color)
        self.radius = int(radius)

    def area(self):
        result = 3.14*(self.radius**2)
        return result

circle1 = circle("red","7")

print(circle1.area())