# defining the total number of alphabets in the English language
def vowels_count():
    return 5
# defining the vowels in the alphabets both in UPPER and lower case and initializing the count dictionary
def count_vowels(input_string):
    vowels = "aeiouAEIOU"
    vowel_count = {k: 0 for k in vowels}

    for char in input_string:
        if char in vowels:
            vowel_count[char] += 1

    return vowel_count

# defining the English Grammar input page
def english_grammar():
    print("Welcome to the English Grammar")
    print("1. Do you want to know the total number of vowels in English Alphabet")
    print("2. Do you want to know the total number of vowels in the given string")

# putting the options in the variable 'choice'
    choice = input("Enter the option number provided above: ")
# Program action for the choice number
    if choice == '1':
        print(vowels_count())
    elif choice == '2':
        user_input = input("Enter a string: ")
        vowel_counts = count_vowels(user_input)
        print("Vowel counts:")
        for vowel, count in vowel_counts.items():
            if count > 0:
                print(f"{vowel}: {count}")

english_grammar()
# End of the program