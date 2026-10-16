# - ใหนักศึกษาเขียนโปรแกรม ที่มีฟังก์ชันต่อไปนี้
# - ฟังก์ชันชื่อ countChar เพื่อนับจํานวนตัวอักษรใน String
# เช่น print( countChar( "a" , "Thailand" ) )
# จะแสดงค่า 2 เพราะมีa สองตัวในคําว่า Thailand

# - ฟังก์ชันชื่อ countVowels เพื่อนับจํานวนตัวสระ (aeiou) ใน String
# เช่น print( countVowels("Bangkok") )
# จะแสดงค่า 2 เพราะมีสระสองตัวในคําว่า Bangkok
# และฟังก์ชันนี้ต้องมีการเรียกใช้ countChar() สําหรับหาจํานวนตัวอักษร

# - ฟังก์ชันชื่อ countWords เพื่อนับจํานวนคํา ใน String
# เช่น print( countWords("Human and AI can make mistakes") )
# จะแสดงค่า 6 เพราะมีสระสองตัวในคําว่า Bangkok


def count_char(word,letter):
    i = 0
    letter_count = 0

    while i < len(word):
        if word[i] == letter:
            letter_count += 1
        i += 1

    return letter_count

def countVowels(word):
    # 1. กำหนดสระที่เราต้องการหา
    vowels = "aeiou"
    total_vowels = 0
    i = 0
    
    # 2. วนลูปทีละตัวอักษรในคำว่า vowels (เช็ค 'a', 'e', 'i', 'o', 'u' ทีละตัว)
    while i < len(vowels):
        current_vowel = vowels[i]
        
        # 📌 จุดสำคัญ: เรียกใช้ฟังก์ชันแรก (count_char) ตรงนี้!
        # ส่งคำว่า word และสระตัวปัจจุบันไปให้นับ แล้วเอาผลลัพธ์มาบวกสะสม
        total_vowels += count_char(word, current_vowel)
        
        i += 1
        
    return total_vowels

# ทดสอบใช้งานตามโจทย์




word_input = input("word: ")
letter_input = input("letter: ")


print(count_char(word_input,letter_input))
print(countVowels("Bangkok"))  # จะแสดงค่า 2 (มี a และ o)