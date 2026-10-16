name = ["jame","jabra","jack","john","jill"]
score = [85,42,67,73,50]


for i in score:

    if i >= 80:
            grade = "A"
    elif i >= 70:
        grade = "B"
    elif i >= 60:
        grade = "C"
    elif i >= 50:
        grade = "E"
    else:
        grade = "F"
            
for e in name:
    print(f"เด็กชาย {e} ได้คะแนน {i} ได้เกรด {grade}")