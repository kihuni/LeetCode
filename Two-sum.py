# Given an array of intergers nums and an interger target, return indicess of two numbers such that they add up to the target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.

# You can return the answer in any order.
"""
input = [2, 7, 11, 15], target = 9
Output = [0, 1]
explanation: Because nums[0] + nums[1] == 9, we return [0, 1]

Example 2:
input = [3, 2, 4], target = 6
Output = [1, 2]

Example 3:
inpuut = [3, 3], target = 6
Output = [0, 1]

Constraints:
2 <= nums.length <= 10^3
-10^9 <= nums[i] <= 10^9
-10^9 <= target <= 10^9

Only one valid answer exists.


follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""

def two_sum(nums, target):
    # create a dictionary to store the value and index
    dict = {}
    # loop through the list
    for i in range(len(nums)):
        # check if the difference between the target and the current number is in the dictionary
        if target - nums[i] in dict:
            # if it is, return the index of the difference and the current index
            return [dict[target - nums[i]], i]
        # else, add the number and the index to the dictionary
        dict[nums[i]] = i
    return []

print(two_sum([2,7,11,15], 9))
