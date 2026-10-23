vowels = ["a", "e", "i", "o", "u"]

def countVowels(word):
    word = word.lower()
    count = 0
    i = 0
    while i < len(word):
        if word[i] in vowels:
            count += 1
        i += 1
    return count

print(countVowels("my name is meow"))  