#
# [7] Reverse Integer
#
# https://leetcode.com/problems/reverse-integer/description/
#
# algorithms
# Easy (24.39%)
# Total Accepted:    457.5K
# Total Submissions: 1.9M
# Testcase Example:  '123'
#
# Given a 32-bit signed integer, reverse digits of an integer.
#
# Example 1:
#
#
# Input: 123
# Output: 321
#
#
# Example 2:
#
#
# Input: -123
# Output: -321
#
#
# Example 3:
#
#
# Input: 120
# Output: 21
#
#
# Note:
# Assume we are dealing with an environment which could only store integers
# within the 32-bit signed integer range: [−2^31,  2^31 − 1]. For the purpose of
# this problem, assume that your function returns 0 when the reversed integer
# overflows.
#
#
class Solution:
    def reverse(self, x, lower_limit = -2**31, upper_limit = 2**31-1):
        """
        :type x: int
        :rtype: int
        """

        flag = 1 if x >= 0 else -1
        new_x, x = 0, abs(x)
        while x:
            new_x = 10 * new_x + x % 10
            x //= 10
        new_x = flag * new_x
        return new_x if new_x <= upper_limit and new_x >= lower_limit else 0
