python3 队列

```
import queue

# 基本操作
q = queue.Queue()
q.empty()
q.put()
q.get()
```

主要思路是：
用一个队列来做，本质还是从上往下的层序遍历，最后把结果倒一下

有递归解法和非递归的迭代解法
