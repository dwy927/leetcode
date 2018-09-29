#
# [190] Reverse Bits
#
# https://leetcode.com/problems/reverse-bits/description/
#
# algorithms
# Easy (29.26%)
# Total Accepted:    150.8K
# Total Submissions: 515.3K
# Testcase Example:  '    43261596 (00000010100101000001111010011100)'
#
# Reverse bits of a given 32 bits unsigned integer.
#
# Example:
#
#
# Input: 43261596
# Output: 964176192
# Explanation: 43261596 represented in binary as
# 00000010100101000001111010011100,
# return 964176192 represented in binary as 00111001011110000010100101000000.
#
#
# Follow up:
# If this function is called many times, how would you optimize it?
#
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n = ((n&0xffff0000) >> 16) | ((n&0x0000ffff) << 16)
        n = ((n&0xff00ff00) >> 8) | ((n&0x00ff00ff) << 8)
        n = ((n&0xf0f0f0f0) >> 4) | ((n&0x0f0f0f0f) << 4)
        n = ((n&0xcccccccc) >> 2) | ((n&0x33333333) << 2)
        n = ((n&0xaaaaaaaa) >> 1) | ((n&0x55555555) << 1)
        return n
