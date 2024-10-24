def longest_common_substring(str1, str2):
# assigning the length of the string1 and string2 to 'm' and 'n'
    m, n = len(str1), len(str2)
    longest_length = 0
    ending_index = 0

#defining dp
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Build the dp array
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
                if dp[i][j] > longest_length:
                    longest_length = dp[i][j]
                    ending_index = i  # Update ending index of the substring
            else:
                dp[i][j] = 0

    # Extract the longest common substring
    if longest_length == 0:
        return ""
    else:
        return str1[ending_index - longest_length: ending_index]



string1 = input("Enter the first string: ")
string2 = input("Enter the second string: ")
result = longest_common_substring(string1, string2)
print("Longest common substring:", result)
#End of the program