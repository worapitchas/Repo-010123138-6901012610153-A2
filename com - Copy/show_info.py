name = str(input("Enter your name: "))

def show_info():
    print("This program will calculate area of a land")
    print("given width and length")
    print(f"created by {name}")

def get_width():
    width = float(input("Enter the width of the land: "))
    return width

def get_length():
    length = float(input("Enter the length of the land: "))
    return length

def cal_area(width, length):
    area = width * length
    return area

def show_area(area):
    print(f"The area of the land is: {area} square units")

def show_area_in_SqWa(area):
    area_in_sqwa = area / 4
    print(f"The area of the land in square wa is: {area_in_sqwa} sq.wa")

show_info()
width = get_width() 
length = get_length()
area = cal_area(width, length)
show_area(area)
show_area_in_SqWa(area)