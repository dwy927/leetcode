#
# [5] Longest Palindromic Substring
#
# https://leetcode.com/problems/longest-palindromic-substring/description/
#
# algorithms
# Medium (25.89%)
# Total Accepted:    431.3K
# Total Submissions: 1.7M
# Testcase Example:  '"babad"'
#
# Given a string s, find the longest palindromic substring in s. You may assume
# that the maximum length of s is 1000.
#
# Example 1:
#
#
# Input: "babad"
# Output: "bab"
# Note: "aba" is also a valid answer.
#
#
# Example 2:
#
#
# Input: "cbbd"
# Output: "bb"
#
#
#
class Solution:

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        maxlen = 1
        start = 0
        end = 0

        dp = [[False for x in range(len(s))] for x in range(len(s))]
        for i in range(len(s)): # end
            for j in range(0, i): # start
                dp[j][i] = s[i] == s[j] and (i-j<2 or dp[j+1][i-1])
                if dp[j][i] and maxlen < (i-j+1):
                    maxlen = i-j+1
                    start, end = j, i
            dp[i][i] = True
        return s[start:end+1]
