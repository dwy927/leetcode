最暴力的方法：
把遇到的Node记到set里面，然后看有没有重复。
但空间复杂度不是O(1)
本质上不符合题目要求

如果有交叉
headA：会走过 x + z
headB：会走过 y + z

思路一：
A和B的尾端，如果交叉必然一致，
由此可以把 A，B 中长出那段截掉，然后两边每次各移动一步，找下去一样的就行。
但这个，需要先把A，B都遍历一遍，得到A，B的长度
```
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        lenA = self.getListLen(headA)
        lenB = self.getListLen(headB)
        if lenA > lenB:
            for i in range(lenA - lenB):
                headA = headA.next
        elif lenA < lenB:
            for i in range(lenB - lenA):
                headB = headB.next
        while headA != headB:
            headA, headB = headA.next, headB.next
        return headA

    def getListLen(self, head):
        length = 0
        while head:
            length += 1
            head = head.next
        return length
```

思路二：
走完A后接着走B：当走到 (x + z) + y
走完B后接着走A：当走到 (y + z) + x
的时候，就能找到交叉点
```
class Solution(object):
    def getIntersectionNode(self, headA, headB):
        if not headA or not headB:
            return None
        p, q = headA, headB
        while p and q and p != q:
            p = p.next
            q = q.next
            if p == q:
                return p
            if not p:
                p = headB
            if not q:
                q = headA
        return p
```
