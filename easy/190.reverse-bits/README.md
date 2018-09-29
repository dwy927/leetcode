十进制转二进制 `bin(x)` 有前缀0b
十进制转八进制 `oct(x)` 有前缀0o
十进制转十六进制 `hex(x)` 有前缀0x

二进制转十进制 `int('100', 2)` 这个不需要0b的前缀
八进制转十进制 `int('04', 4)`
十六进制转十进制 `int('0x4', 16)`

题目要求：颠倒给定的32位无符号整数的二进制位

解法一：最粗暴的做法
```
class Solution:
    def reverseBits(self, n):
        rev_n = bin(n)[2::]
        rev_n = "{:0>32d}".format(int(rev_n))
        rev_n = rev_n[::-1]
        return int(rev_n, 2)
```
注意题目强调了32位，所以不足32位前面要补0，倒一倒会在后面

解法二: O(n)
依次把n的每一位从低到高取出来，然后从另一个方向往前推，重复32位
```
class Solution:
    def reverseBits(self, n):
        ret = 0
        for _ in range(32):
            ret <<= 1
            ret |= (n & 1)
            n >>= 1
        return ret
```

解法三: O(log(n))
```
class Solution:
    def reverseBits(self, n):
        n = ((n&0xffff0000) >> 16) | ((n&0x0000ffff) << 16)
        n = ((n&0xff00ff00) >> 8) | ((n&0x00ff00ff) << 8)
        n = ((n&0xf0f0f0f0) >> 4) | ((n&0x0f0f0f0f) << 4)
        n = ((n&0xcccccccc) >> 2) | ((n&0x33333333) << 2)
        n = ((n&0xaaaaaaaa) >> 1) | ((n&0x55555555) << 1)
        return n
```
