def cal_grade(score):
    print(f"คะแนน {score}")
    if 100 >= score >= 80:
        grade = "A"
    elif 79 >= score >= 70:
        grade = "B"
    elif 69 >= score >=60:
        grade = "C"
    elif 59 >= score >=50:
        grade = "D"
    elif score >= 0 :
        grade = "F"
    else:
        grade = "error"
    return grade

score = float(input("score : "))
result = cal_grade(score)
print(f"ได้เกรด {result}")