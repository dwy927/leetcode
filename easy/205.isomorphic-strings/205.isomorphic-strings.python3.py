#
# [205] Isomorphic Strings
#
# https://leetcode.com/problems/isomorphic-strings/description/
#
# algorithms
# Easy (36.18%)
# Total Accepted:    175.9K
# Total Submissions: 486.1K
# Testcase Example:  '"egg"\n"add"'
#
# Given two strings s and t, determine if they are isomorphic.
#
# Two strings are isomorphic if the characters in s can be replaced to get t.
#
# All occurrences of a character must be replaced with another character while
# preserving the order of characters. No two characters may map to the same
# character but a character may map to itself.
#
# Example 1:
#
#
# Input: s = "egg", t = "add"
# Output: true
#
#
# Example 2:
#
#
# Input: s = "foo", t = "bar"
# Output: false
#
# Example 3:
#
#
# Input: s = "paper", t = "title"
# Output: true
#
# Note:
# You may assume both s and t have the same length.
#
#
class Solution:
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False

        dic1 = dict()
        dic2 = dict()
        idx = 0
        for x, y in zip(s, t):
            if x in dic1.keys() and y in dic2.keys():
                if dic1[x] != dic2[y]:
                    return False
            elif x not in dic1.keys() and y not in dic2.keys():
                dic1[x], dic2[y] = idx, idx
                idx += 1
            else:
                return False
        return True
