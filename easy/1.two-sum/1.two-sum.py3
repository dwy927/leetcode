#
# [1] Two Sum
#
# https://leetcode.com/problems/two-sum
#
# algorithms
# Easy (36.12%)
# Total Accepted:    699.4K
# Total Submissions: 1.9M
# Testcase Example:  '[3,2,4]\n6'
#
# Given an array of integers, return indices of the two numbers such that they
# add up to a specific target.
#
# You may assume that each input would have exactly one solution, and you may
# not use the same element twice.
#
#
# Example:
#
# Given nums = [2, 7, 11, 15], target = 9,
#
# Because nums[0] + nums[1] = 2 + 7 = 9,
# return [0, 1].
#
#
#
class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {}
        for index, num in enumerate(nums):
          if target - num in dic:
            return[dic[target-num], index]
          else:
            dic[num] = index
