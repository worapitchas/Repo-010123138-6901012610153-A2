score = float(input("คะแนน : "))

if 100 >= score >= 81:
    print("great!")
elif 80 >= score >= 51:
    print("pass!")
elif 50 >= score >= 0:
    print("failed!")
else:
    print("error!")