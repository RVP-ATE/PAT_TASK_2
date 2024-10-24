# defining the function tp count the words in the given string
def count_words(input_string):
    # Split the string into words and count them
    words = input_string.split()
    return len(words)

# input the string to calculate
input_string = input("Enter a string: ")
word_count = count_words(input_string)
print(f"The number of words in the string is: {word_count}")
# End of the program
