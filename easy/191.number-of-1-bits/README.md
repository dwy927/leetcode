计算汉明重量(位1的个数)

方法1: 移位法

使用将n不断右移，并与1想&得到1的个数

时间复杂度:`O(logn)`，因为有`logn`位

```python3
class Solution(object):
    def hammingWeight(self, n):
        ret = 0
        while n > 0:
            ret += (n & 1)
            n >>= 1
        return ret
```

方法2: n&(n-1)

假使 n =0x110101
                n                       n-1              n&(n-1)
step1:   110101          110100          110100
step2:   110100          110011          110000
step3:   110000          101111          100000
step4:   100000          011111          000000

发现有几个1，就循环几次n&(n-1)得到0，明显较于上者运行效率更高些。

本质上：n&(n-1)可以把n的最低位的1消除掉

时间复杂度：`O(M)`,M是n中1的个数

```python3
class Solution(object):
    def hammingWeight(self, n):
        ret = 0
        while n > 0:
            n &= (n-1)
            ret += 1
        return ret
```

