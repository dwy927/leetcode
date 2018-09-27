空间复杂度为O(n):
位置在i的数字，会被移动到 (i+k)%n
```
class Solution:
    def rotate(self, nums, k):
        n = len(nums)
        ret = [x for x in nums]
        for i in range(n):
            idx = (i + k) % n
            nums[idx] = ret[i]
        return
```



空间复杂度要为O(1):

主要的难度在于，要一个原地算法的话，注意原值覆盖的问题。

主要步骤如下：

1. 把数组分成两部分，前面有n-k个数，后面k个数
2. 前半部分中心对应翻转；
3. 后半部分中心对应翻转；
4. 整个数组中心对应翻转；

![img](/Users/dwy/code/leetcode/easy/189.rotate-array/img.png)

算法实现注意下标
