# Defining the function to find matches and able to create new word "Relates to anagram"
def anagrams(str1, str2):
    # Remove spaces and convert to lowercase
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Sort the characters and compare
    return sorted(str1) == sorted(str2)


string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")

# Defining the condition and calling the function
if anagrams(string1, string2):
    print("True: The strings are anagrams.")
else:
    print("False: The strings are not anagrams.")
# End of the Program