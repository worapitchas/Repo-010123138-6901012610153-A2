# a. search for a character in a string (return index),
# starting from the left-hand side (index=0 )

# b. search for a character in a string (return index),
# starting from the right-hand side (index=length-1)

# e. boolean function to check whether a given string is a palindrome
# (using while loop) start with simple strings


def count_char():
    word = "Baitong"

    i = 0
    word_count = 0

    while i < len(word):
        
        word_count += 1
        i += 1

    return word_count

print(count_char())

def search_char(search):
    word = "Baitong"
    word_clean = word.lower()
    search_clean = search.lower()

    i = 0
    
    word_count = 0

    while i < len(word_clean):
       
        if search_clean == word_clean[i]:

            return i
        i += 1
    return False

def search_char_back(search):
    word = "Baitong"
    word_clean = word.lower()
    search_clean = search.lower()

    i = 0
    
    word_count = 0

    i = len(word_clean)-1

    while i >= 0:
       
        if search_clean == word_clean[i]:

            return i
        i -= 1
    return False


def check_palin():
    word = "Bab"
    word_clean = word.lower()
    word_reverse = ""

    i = len(word_clean) - 1

    while i >= 0:
        word_reverse = word_reverse + word_clean[i]
        i -= 1

    
    if word_clean[i] == word_reverse[i]:
        return True
    else:
        return False

your_search = input("search your letter: ")

print(count_char())
print(search_char(your_search))
print(search_char_back(your_search))
print(check_palin())



