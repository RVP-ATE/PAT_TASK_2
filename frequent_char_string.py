# defining the function for the connecting the two string and find most frequent char
def most_frequent_char(str1, str2):
    # Combine the two strings
    combined_str = str1 + str2

    # Create a dictionary to count character frequencies
    char_count = {}

    # Count the frequency of each character
    for char in combined_str:
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1

    # Find the character with the maximum frequency
    most_common_char = None
    most_common_count = 0

    for char, count in char_count.items():
        if count > most_common_count:
            most_common_char = char
            most_common_count = count

    return most_common_char, most_common_count



string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
char, count = most_frequent_char(string1, string2)

if char:
    print(f"The most frequent character is '{char}' with a frequency of {count}.")
else:
    print("No characters found.")
# End of the program