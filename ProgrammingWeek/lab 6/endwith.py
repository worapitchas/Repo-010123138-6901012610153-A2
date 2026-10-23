def custom_endswith(string, suffix):
    if len(suffix) > len(string) or len(string) == 0:
        return False
    i = len(string) - 1
    j = len(suffix) - 1
    while j >= 0:
        if string[i] != suffix[j]:
            return False
        i -= 1
        j -= 1
    return True


filename = "my_avatar.png"


if custom_endswith(filename, ".png") or custom_endswith(filename, ".jpg"):
    print("อัปโหลดไฟล์รูปภาพสำเร็จ!")
else:
    print("ปฏิเสธการอัปโหลด: รองรับเฉพาะไฟล์ .png และ .jpg เท่านั้น")
