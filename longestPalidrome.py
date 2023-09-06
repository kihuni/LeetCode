def longestPalindrome(s: str) -> str:
    # if the string is empty or has length 1, return the string itself
    if len(s) == 0 or len(s) == 1:
        return s
    
    # This function finds the length of palindrome with center (left, right)
    def expandFromCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindromic substring
        return s[left+1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome (center is i)
        palindrome1 = expandFromCenter(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        
        # Even-length palindrome (center is i and i+1)
        palindrome2 = expandFromCenter(i, i+1)
        if len(palindrome2) > len(longest):
            longest = palindrome2
            
    return longest
def longestPalindrome(s: str) -> str:
    # if the string is empty or has length 1, return the string itself
    if len(s) == 0 or len(s) == 1:
        return s
    
    # This function finds the length of palindrome with center (left, right)
    def expandFromCenter(left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        # Return the palindromic substring
        return s[left+1:right]
    
    longest = ""
    for i in range(len(s)):
        # Odd-length palindrome (center is i)
        palindrome1 = expandFromCenter(i, i)
        if len(palindrome1) > len(longest):
            longest = palindrome1
        
        # Even-length palindrome (center is i and i+1)
        palindrome2 = expandFromCenter(i, i+1)
        if len(palindrome2) > len(longest):
            longest = palindrome2
            
    return longest

s1 = "babad"
print(longestPalindrome(s1))  # Output: "bab" (or "aba")

s2 = "cbbd"
print(longestPalindrome(s2))  # Output: "bb"
