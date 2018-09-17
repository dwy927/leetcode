https://leetcode-cn.com/problems/linked-list-cycle/solution/

最naive的解法是：
找个set把遇到过的node存下来，对每个新节点看是不是在set里面出现过
空间复杂度最差为$O(n)$

比较高级的做法：
通过使用具有不同速度的快、慢两个指针遍历链表，空间复杂度可以被降低至 O(1)。慢指针每次移动一步，而快指针每次移动两步。

```
public boolean hasCycle(ListNode head) {
    if (head == null || head.next == null) {
        return false;
    }
    ListNode slow = head;
    ListNode fast = head.next;
    while (slow != fast) {
        if (fast == null || fast.next == null) {
            return false;
        }
        slow = slow.next;
        fast = fast.next.next;
    }
    return true;
}
```
