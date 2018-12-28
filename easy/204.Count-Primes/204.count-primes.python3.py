#
# [204] Count Primes
#
# https://leetcode.com/problems/count-primes/description/
#
# algorithms
# Easy (27.62%)
# Total Accepted:    198.3K
# Total Submissions: 717.8K
# Testcase Example:  '10'
#
# Count the number of prime numbers less than a non-negative number, n.
#
# Example:
#
#
# Input: 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
#
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n <= 2:
            return 0

        flags = [True] * n
        flags[0] = False # 1不是质数
        for i in range(2, int(n**0.5) + 1):
            if flags[i-1]:
                for x in range(i*2, n, i):
                    flags[x-1] = False


        return sum(flags[:-1]) # 小于n的数中有多少个质数
