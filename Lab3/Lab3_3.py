def count_letters(text):
    letter_count = {}
    for char in text:
        if char.isalpha() and char.islower():
            char = char.lower()
            letter_count[char] = letter_count.get(char, 0) + 1
    return letter_count

def calculate_frequency(letter_count):
    total_letters = sum(letter_count.values())
    frequency_dict = {}
    for letter, count in letter_count.items():
        frequency = count / total_letters
        frequency_dict[letter] = frequency
    return frequency_dict

def print_frequency(frequency_dict):
    for letter, frequency in frequency_dict.items():
        print(f"{letter}: {frequency:.2f}")

text = "Е1сли нет в2етра, б3еритесь з4а в5ёсла"

letter_count = count_letters(text)

frequency_dict = calculate_frequency(letter_count)

print_frequency(frequency_dict)
