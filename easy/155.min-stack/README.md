MinStack：
```
def getMin(self):
      return min(self.stack)
```
不直接用min

1. 维护一个最小值 minValue：
初始化的时候多定义了一个最小值self.min,在每次push和pop操作的时候就判断是否为最小值，保证self.min是最小的
https://blog.csdn.net/qq_34364995/article/details/80518193

2. 维护一个最小栈 minStack
栈中的最小元素会在压栈和弹出两个操作中发生改变，
如果仅用一个变量来表示当前栈中的最小元素，压栈时更新该变量没有问题，
但弹出时，如果弹出的就是最小的元素，那剩下栈中最小的元素需要O(n)的时间重新找出，不符合题目要求。

我们可以通过另外一个栈来存储当前栈中的最小元素。
在压栈时，如果最小栈的栈顶元素大于等于压入的元素，那么要对最小栈也进行压栈操作。
而在弹出时，如果栈中弹出的元素与最小栈栈顶的元素相等，那我们也要对最小栈进行弹出，
最小栈在弹出后，栈顶元素仍然是当前栈中最小的元素。
https://shenjie1993.gitbooks.io/leetcode-python/155%20Min%20Stack.html

法2是比较好的解法
