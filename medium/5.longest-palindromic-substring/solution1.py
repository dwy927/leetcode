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

    def getLongest(self, s, start, end):
        if start == end:
            return 1
        if start > end:
            return 0

        while s[start] != s[end]:
            start += 1
        if s[start:end+1] == s[start:end+1][::-1]:
            return end - start + 1
        else:
            return self.getLongest(s, start+1, end)

    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) == 0:
            return ""

        dp = [0] * len(s)
        max, maxidx = 1, 0
        for idx, x in enumerate(s):
            if idx == 0:
                dp[0] = 1
                continue
            tmp = dp[idx-1]
            iidx = idx - tmp -1
            if iidx >= 0:
                if x == s[iidx]:
                    dp[idx] = dp[idx-1] + 2
                    if dp[idx] > max:
                        max = dp[idx]
                        maxidx = idx
                    continue
            dp[idx] = self.getLongest(s, iidx+1, idx)
            if dp[idx] > max:
                max = dp[idx]
                maxidx = idx
        tmp = maxidx - max + 1
        return s[tmp: maxidx + 1]
