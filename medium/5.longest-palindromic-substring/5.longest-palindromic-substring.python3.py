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
        if s == "":
            return ""

        ss = '^'
        for x in s:
            ss += '#' + x
        ss += '#$'

        dp = [0] * len(ss) # 记录半径，包括自己
        mid = 1 # 起始中心点是1
        mx = 1 # 起始最远点也是1
        maxLen = 1
        maxMid = 1
        for i in range(1, len(ss)-1):
            if i < mx:
                dp[i] = min(dp[2*mid-i], mx-i+1)
            else:
                dp[i] = 1
            while ss[i + dp[i]] == ss[i - dp[i]]:
                dp[i] += 1
            if i + dp[i] - 1> mx: # 一直刷最远点
                mx = i + dp[i] - 1
                mid = i
            if dp[i] > maxLen: # 一直刷最长的子串
                maxLen = dp[i]
                maxMid = i
        left = (maxMid - (maxLen - 1))//2
        right = (maxMid + (maxLen -1))//2

        return s[left:right]
