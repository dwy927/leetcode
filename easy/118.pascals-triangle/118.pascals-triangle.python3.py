#
# [118] Pascal's Triangle
#
# https://leetcode.com/problems/pascals-triangle/description/
#
# algorithms
# Easy (41.59%)
# Total Accepted:    192.7K
# Total Submissions: 459.7K
# Testcase Example:  '5'
#
# Given a non-negative integer numRows, generate the first numRows of Pascal's
# triangle.
#
#
# In Pascal's triangle, each number is the sum of the two numbers directly
# above it.
#
# Example:
#
#
# Input: 5
# Output:
# [
# ⁠    [1],
# ⁠   [1,1],
# ⁠  [1,2,1],
# ⁠ [1,3,3,1],
# ⁠[1,4,6,4,1]
# ]
#
#
#
class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        ret = []
        if numRows == 0:
            return ret
        for i in range(numRows):
            if i == 0:
                cur = [1]
            else:
                pre = ret[-1]
                cur = [1] + [pre[idx] + pre[idx+1] for idx in range(len(pre) - 1)] + [1]
            ret.append(cur)
        return ret
