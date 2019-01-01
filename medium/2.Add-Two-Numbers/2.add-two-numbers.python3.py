#
# [2] Add Two Numbers
#
# https://leetcode.com/problems/add-two-numbers/description/
#
# algorithms
# Medium (29.92%)
# Total Accepted:    690.9K
# Total Submissions: 2.3M
# Testcase Example:  '[2,4,3]\n[5,6,4]'
#
# You are given two non-empty linked lists representing two non-negative
# integers. The digits are stored in reverse order and each of their nodes
# contain a single digit. Add the two numbers and return it as a linked list.
#
# You may assume the two numbers do not contain any leading zero, except the
# number 0 itself.
#
# Example:
#
#
# Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
# Output: 7 -> 0 -> 8
# Explanation: 342 + 465 = 807.
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode(0)
        x = 0
        before = ListNode(0)
        before.next = head
        while l1 != None and l2 != None:
            x += l1.val + l2.val
            cur = before.next
            cur.val = x % 10
            x = x // 10
            cur.next = ListNode(x)
            l1, l2, before = l1.next, l2.next, cur

        if l1 != None:
            l1.val += x
            before.next = l1
        if l2 != None:
            l2.val += x
            before.next = l2

        cur = before.next
        while cur.val > 9:
            cur.val = 0
            cur, before = cur.next, cur
            if cur == None:
                before.next = ListNode(0)
            cur = before.next
            cur.val += 1

        if cur.val == 0 and cur.next == None:
            before.next = None

        return head
