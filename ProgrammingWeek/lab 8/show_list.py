import os


folder = "."


total_size = 0
image_size = 0

print("=== รายชื่อไฟล์ทั้งหมด ===")


for file in os.listdir(folder):

  
    if os.path.isfile(file):
        size = os.path.getsize(file)  
        total_size += size  
        print(f"ไฟล์: {file} | ขนาด: {size} Bytes")

print(f"\n>> ขนาดไฟล์รวมทั้งหมด: {total_size} Bytes")
print("=" * 40)

print("=== รายชื่อเฉพาะไฟล์รูปภาพ ===")


for file in os.listdir(folder):

    if os.path.isfile(file):
      
        if (
            file.endswith(".jpg")
            or file.endswith(".png")
            or file.endswith(".gif")
        ):
            size = os.path.getsize(file)
            image_size += size  
            print(f"รูปภาพ: {file} | ขนาด: {size} Bytes")

print(f"\n>> ขนาดรวมเฉพาะไฟล์รูปภาพ: {image_size} Bytes")