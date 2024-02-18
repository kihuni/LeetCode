# given two sorted arrays num1 and nums2 of size m and n respectively, return the median of the two sorted arrays
# The overall run time complexity should be O(log(m+n))


# example 1:

# Input: nums1 = [1, 3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1, 2, 3] and median is 2

# example 2:
# Input: nums1 = [1, 2], nums2 = [3, 4]
# Output: 2.50000
# Explanation: merged array = [1, 2, 3, 4] and median is (2 + 3) / 2 = 2.5

# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -10^6 <= nums1[i], nums2[i] <= 10^6


class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # Merge the two sorted arrays
        nums1.extend(nums2)
        # Sort the merged array
        nums1.sort()
        # Get the length of the merged array
        n = len(nums1)
        # Check if the length is even
        if n % 2 == 0:
            # If even, return the average of the two middle elements
            return (nums1[n//2] + nums1[n//2 - 1]) / 2
        else:
            # If odd, return the middle element
            return nums1[n//2]
