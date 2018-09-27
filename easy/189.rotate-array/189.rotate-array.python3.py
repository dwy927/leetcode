#
# [189] Rotate Array
#
# https://leetcode.com/problems/rotate-array/description/
#
# algorithms
# Easy (26.94%)
# Total Accepted:    218.3K
# Total Submissions: 810.1K
# Testcase Example:  '[1,2,3,4,5,6,7]\n3'
#
# Given an array, rotate the array to the right by k steps, where k is
# non-negative.
#
# Example 1:
#
#
# Input: [1,2,3,4,5,6,7] and k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
#
#
# Example 2:
#
#
# Input: [-1,-100,3,99] and k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]
#
#
# Note:
#
#
# Try to come up as many solutions as you can, there are at least 3 different
# ways to solve this problem.
# Could you do it in-place with O(1) extra space?
#
#
#
class Solution:
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        k %= n
        m = n-k
        # 前半部分
        for i in range(m//2):
            tmp = nums[i]
            nums[i] = nums[m-i-1]
            nums[m-i-1] = tmp

        # 后半部分
        for i in range(k//2):
            idx = i + m
            tmp = nums[idx]
            nums[idx] = nums[n-i-1]
            nums[n-i-1] = tmp

        # 全部翻一遍
        for i in range(n//2):
            tmp = nums[i]
            nums[i] = nums[n-i-1]
            nums[n-i-1] = tmp
        return
