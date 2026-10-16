eggs = int(input("จำนวนไข่ : "))
oil = eggs


print("ตอกไข่ ", eggs , "ฟอง")
print("ตีไข่")
print("ตั้งกระทะให้ร้อน")

while True:
    menu = str(input("ต้องการไข่ทอดแบบไหน (ฟู/นุ่ม/คลีน) : "))
    
    if menu == "ฟู":
        print("เทน้ำมัน", oil, "ถ้วยตวง")
        break
    elif menu == "นุ่ม":
        print("เทน้ำมัน", oil, "ช้อนโต๊ะ")
        break
    elif menu =="คลีน":
        print("เทน้ำมัน", oil, "ช้อนชา")
        break
    else:
        print("ไม่มีสูตร")

print("เทไข่ตามลงไป")
print("พลิกไข่")
print("เสิร์ฟบนจาน")

while True:
    sauce = str(input("ต้องการซอสอะไร (มะเขือเทศ/พริก) : "))
    
    if sauce == "มะเขือเทศ":
        print("ราดซอสมะเขือเทศ")
        break
    elif sauce == "พริก":
        print("ราดซอสพริก")
        break
    else:
        print("ไม่มีซอสนี้")

print(f"ไข่เจียว{menu}ราดซอส{sauce}พร้อมเสิร์ฟแล้วค่ะ")

