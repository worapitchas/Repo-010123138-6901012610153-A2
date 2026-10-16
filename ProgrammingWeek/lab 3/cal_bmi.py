
def cal_bmi(weight,height):
    bmi = weight/((height*0.01)**2)
    print(f"น้ำหนัก {weight} ส่วนสูง {height}")
    if bmi < 18.5:
        weight_status = "lower weight"
    elif 29.9 > bmi > 25:
        weight_status = "healthy weight"
    elif bmi > 25:
        weight_status = "over weight"
    return weight_status

weight = float(input("weight : "))
height = float(input("height : "))
result = cal_bmi(weight,height)
print(f"you are {result}")