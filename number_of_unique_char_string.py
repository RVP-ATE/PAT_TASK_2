# defining the function count unique characters in the given string
def count_unique_characters(input_string):
# using the set function for avoid duplicate characters in the input string
    unique_chars = set(input_string)
    return len(unique_chars)
# Enter the string
user_input = input("Enter a string: ")
result = count_unique_characters(user_input)
print("Number of unique characters:", result)
# End of the Program