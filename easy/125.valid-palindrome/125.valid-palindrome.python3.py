#
# [125] Valid Palindrome
#
# https://leetcode.com/problems/valid-palindrome/description/
#
# algorithms
# Easy (28.40%)
# Total Accepted:    262.8K
# Total Submissions: 924.7K
# Testcase Example:  '"A man, a plan, a canal: Panama"'
#
# Given a string, determine if it is a palindrome, considering only
# alphanumeric characters and ignoring cases.
#
# Note: For the purpose of this problem, we define empty string as valid
# palindrome.
#
# Example 1:
#
#
# Input: "A man, a plan, a canal: Panama"
# Output: true
#
#
# Example 2:
#
#
# Input: "race a car"
# Output: false
#
#
#
class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        n = len(s)
        left = 0
        right = n-1
        while left < right:
            l = s[left]
            if not l.isdigit() and not l.isalpha():
                left += 1
                continue
            r = s[right]
            if not r.isdigit() and not r.isalpha():
                right -= 1
                continue
            if l != r:
                return False
            else:
                left += 1
                right -= 1
        return True
