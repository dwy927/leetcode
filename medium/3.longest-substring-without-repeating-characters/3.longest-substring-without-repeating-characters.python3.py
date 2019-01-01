#
# [3] Longest Substring Without Repeating Characters
#
# https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
#
# algorithms
# Medium (25.65%)
# Total Accepted:    684.2K
# Total Submissions: 2.7M
# Testcase Example:  '"abcabcbb"'
#
# Given a string, find the length of the longest substring without repeating
# characters.
#
#
# Example 1:
#
#
# Input: "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
#
#
#
# Example 2:
#
#
# Input: "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
#
#
#
# Example 3:
#
#
# Input: "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# ⁠            Note that the answer must be a substring, "pwke" is a
# subsequence and not a substring.
#
#
#
#
#
#
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        dp = [0] * len(s)
        ss = {}
        for idx, x in enumerate(s):
            if idx == 0:
                dp[0] = 1
                ss[x] = 0
                continue
            if x not in ss.keys():
                dp[idx] = dp[idx-1] + 1
            else:
                dp[idx] = min(dp[idx-1] + 1, idx - ss[x])
            ss[x] = idx
        return max(dp)
