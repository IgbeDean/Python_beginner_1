text = input("Enter a string: ")

def analyse_input(text):
    count_vowels = 0
    count_consonants = 0
    count_digits = 0

    text = text.lower()
    for char in text:
        if char.isdigit():
            count_digits += 1
        elif char.isalpha():
            if char in 'aeiou':
                count_vowels += 1
            else:
                count_consonants += 1
    return count_vowels, count_consonants, count_digits

count_vowels, count_consonants, count_digits = analyse_input(text)

print(f"Vowels: {count_vowels}, Consonants: {count_consonants}, Digits: {count_digits}")