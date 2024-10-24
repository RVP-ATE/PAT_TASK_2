# defining the function remove vowels and assigning the aeiouAEIOU to vowels variable
def remove_vowels(input_string):
    vowels = "aeiouAEIOU"
    return ''.join(char for char in input_string if char not in vowels)
# Enter the input string
user_input = input("Enter the String: ")
result = remove_vowels(user_input)
# Result
print("string with ovwels removed:", result)
# End of the program