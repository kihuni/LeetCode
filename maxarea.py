# you are given an integer arrar height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, height[i]) and (i, 0). 
# and (i, height[i]). Find two lines, which, together with the x-axis forms a container, such that the container contains the most water.
# return the maximum amount of the water a  container can store.

# Notice that you may not slant the container.          
# Example 1:

# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: the above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

# Example 2:
# Input: height = [1,1]
# Output: 1

# Constraints:
# n == height.length
# 2 <= n <= 3 * 10^4
# 0 <= height[i] <= 3 * 10^4

class Solution:
     def maxArea(self, height: List[int]) -> int:
        # Initialize the maximum area
        max_area = 0
        # Initialize the left and right pointers
        left, right = 0, len(height) - 1
        # Loop through the array
        while left < right:
            # Calculate the area
            area = (right - left) * min(height[left], height[right])
            # Update the maximum area
            max_area = max(max_area, area)
            # Move the left and right pointers
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        # Return the maximum area
        return max_area
