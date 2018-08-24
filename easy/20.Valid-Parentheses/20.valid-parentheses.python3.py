#
# [20] Valid Parentheses
#
# https://leetcode.com/problems/valid-parentheses/description/
#
# algorithms
# Easy (34.44%)
# Total Accepted:    382.4K
# Total Submissions: 1.1M
# Testcase Example:  '"()"'
#
# Given a string containing just the characters '(', ')', '{', '}', '[' and
# ']', determine if the input string is valid.
#
# An input string is valid if:
#
#
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
#
#
# Note that an empty string is also considered valid.
#
# Example 1:
#
#
# Input: "()"
# Output: true
#
#
# Example 2:
#
#
# Input: "()[]{}"
# Output: true
#
#
# Example 3:
#
#
# Input: "(]"
# Output: false
#
#
# Example 4:
#
#
# Input: "([)]"
# Output: false
#
#
# Example 5:
#
#
# Input: "{[]}"
# Output: true
#
#
#
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        sList = list(s)
        dic = {')':'(', '}':'{', ']':'['}
        stack = []
        for alpha in sList:
            if alpha in dic.values():
                stack.append(alpha)
            else:
                if len(stack) == 0:
                    return False
                alpha2 = stack.pop()
                if alpha2 != dic[alpha]:
                    return False
        if len(stack) != 0:
            return False
        return True
