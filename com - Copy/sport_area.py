def cal_area(width, length):
    area = width * length
    sports = []
    
    if area >= 105 * 68:
        sports.append("football")
    if area >= 20 * 40:
        sports.append("futsal")
    if area >= 15 * 28:
        sports.append("basketball")
    if area >= 10.97 * 23.77:
        sports.append("tennis")
    if area >= 13.40 * 6.10:
        sports.append("badminton")
    
    return sports

width = float(input("ความกว้าง (เมตร) : "))
length = float(input("ความยาว (เมตร) : "))

result = cal_area(width, length)

result = cal_area(width, length)

if result:
    print("กีฬาที่พื้นที่พอสำหรับเล่นได้แก่:")
    for sport in result:
        print("-", sport)
else:
    print("พื้นที่เล็กเกินไปสำหรับกีฬาข้างต้น")