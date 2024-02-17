# Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range  [-231, 231 - 1], then return 0.
# assume the environment does not allow you to store 64-bit integers (signed or unsigned).


# example 1
# Input: x = 123
# Output: 321

# example 2
# Input: x = -123
# Output: -321

# example 3

# Input: x = 120
# Output: 21

# Constraints:
# -231 <= x <= 231 - 1


# Define a class named Solution.
class Solution:
    # Define a method named reverse that takes an integer x as input and returns an integer.
    def reverse(self, x: int) -> int:
        # If x is negative, reverse the digits of x and make it negative again.
        if x < 0:
            x = -1 * int(str(x)[::-1][:-1])
        # If x is positive, reverse the digits of x.
        else:
            x = int(str(x)[::-1])
        # Check if the reversed integer is within the range of a 32-bit signed integer.
        if x < -2**31 or x > 2**31 - 1:
            return 0
        # Return the reversed integer.
        return x

# Instantiate the Solution class and store it in a variable called solution.
solution = Solution()
# Call the reverse method on the solution object and pass in 123 as the argument.
# Print the result.
print(solution.reverse(123)) # 321
# Call the reverse method on the solution object and pass in -123 as the argument.
# Print the result.
print(solution.reverse(-123)) # -321
# Call the reverse method on the solution object and pass in 120 as the argument.
# Print the result.
print(solution.reverse(120)) # 21
