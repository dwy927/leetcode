#
# [203] Remove Linked List Elements
#
# https://leetcode.com/problems/remove-linked-list-elements/description/
#
# algorithms
# Easy (34.80%)
# Total Accepted:    193.7K
# Total Submissions: 556.5K
# Testcase Example:  '[1,2,6,3,4,5,6]\n6'
#
# Remove all elements from a linked list of integers that have value val.
#
# Example:
#
#
# Input:  1->2->6->3->4->5->6, val = 6
# Output: 1->2->3->4->5
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        while head != None:
            if head.val == val:
                head = head.next
            else:
                break

        if head == None:
            return head

        before = head
        cur = before.next

        while cur != None:
            if cur.val != val:
                before = cur
                cur = cur.next
                continue
            before.next = cur.next
            cur = cur.next

        return head
