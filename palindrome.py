"""
Given an integer x, return true if x is a palindrome, and false otherwise

Example 1:

Input: x = 121
Output: true
Explanation: 121 reads as 121 from left to right and from right to left.
Example 2:

Input: x = -121
Output: false
Explanation: From left to right, it reads -121. From right to left, it becomes 121-. Therefore it is not a palindrome.
Example 3:

Input: x = 10
Output: false
Explanation: Reads 01 from right to left. Therefore it is not a palindrome.
 

Constraints:

-231 <= x <= 231 - 1
 

Follow up: Could you solve it without converting the integer to a string?
"""
class Solution:
    def isPalindrome(self, x: int) -> bool:
        # Negative numbers cannot be palindromes.
        # Numbers ending with 0 aren't palindromes unless the number is 0 itself.
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        reversed_half = 0
        while x > reversed_half:
            reversed_half = reversed_half * 10 + x % 10
            x //=10
            
        # When the length is an odd number, we can get rid of the middle digit by // 10
        # For example when x = 12321, at the end of the loop x = 12, reversed_half = 123, since the middle digit doesn't matter in palindromeness, we can simply get rid of it.
        return x == reversed_half or x == reversed_half // 10


solution = Solution()
print(solution.isPalindrome(121))  # Output: true
print(solution.isPalindrome(-121))  # Output: false
print(solution.isPalindrome(10))   # Output: false