# Given a string s, find the length of the longest 
# substring without repeating characters

#Example 1:

#Input: s = "abcabcbb"
#Output: 3
#Explanation: The answer is "abc", with the length of 3.
#Example 2:

#Input: s = "bbbbb"
#Output: 1
#Explanation: The answer is "b", with the length of 1.
#Example 3:

#Input: s = "pwwkew"
#Output: 3
#Explanation: The answer is "wke", with the length of 3.
#Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.


#Constraints:

#0 <= s.length <= 5 * 104
#s consists of English letters, digits, symbols and spaces.

def length_of_longest_substring(s):
    # Initialize variables
    
    start = 0 # it represents the starting index of the current window or substring
    max_length = 0 # it store the maximum length of the substring without repeating characters
    char_set = set()  # It is a set that will be used to keep track of the characters within the current window
    
    for end in range(len(s)):
            while s[end] in char_set:
                # Remove the character at the start of the window
                char_set.remove(s[start])
                start += 1
            
            # Add the current character to the set
            char_set.add(s[end])
            
            # Update the maximum length 
            max_length = max(max_length, end - start + 1)

    return max_length

# Test cases
s1 = "abcabcbb"
s2 = "bbbbb"
s3 = "pwwkew"

print(length_of_longest_substring(s1))  # Output: 3
print(length_of_longest_substring(s2))  # Output: 1
print(length_of_longest_substring(s3))  # Output: 3