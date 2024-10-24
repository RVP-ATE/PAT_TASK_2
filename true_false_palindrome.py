# defining the function for checking entered string is palindrome or not
def check_palindrome(input_string):
# Normalize the string by removing spaces and converting to lowercase
    normalized_string = ''.join(input_string.split()).lower()
# Check if the normalized string is equal to its reverse
    return normalized_string == normalized_string[::-1]

# Enter the input string to check
user_input = input("Enter a string: ")
result = check_palindrome(user_input)
print("Is the string a palindrome?", result)
#End of the program