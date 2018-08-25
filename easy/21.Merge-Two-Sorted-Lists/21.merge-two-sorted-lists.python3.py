#
# [21] Merge Two Sorted Lists
#
# https://leetcode.com/problems/merge-two-sorted-lists/description/
#
# algorithms
# Easy (42.66%)
# Total Accepted:    392.9K
# Total Submissions: 918.9K
# Testcase Example:  '[1,2,4]\n[1,3,4]'
#
# Merge two sorted linked lists and return it as a new list. The new list
# should be made by splicing together the nodes of the first two lists.
#
# Example:
#
# Input: 1->2->4, 1->3->4
# Output: 1->1->2->3->4->4
#
#
#
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3 = ListNode(0)
        ret = l3
        while l1 != None and l2 != None:
            val1 = l1.val
            val2 = l2.val
            if val1 <= val2:
                l3.next = ListNode(val1)
                l3 = l3.next
                l1 = l1.next
            else:
                l3.next = ListNode(val2)
                l3 = l3.next
                l2 = l2.next
        if l1 != None:
            l3.next = l1
        elif l2 != None:
            l3.next = l2
        return ret.next
