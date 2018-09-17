#
# [141] Linked List Cycle
#
# https://leetcode.com/problems/linked-list-cycle/description/
#
# algorithms
# Easy (34.70%)
# Total Accepted:    295.5K
# Total Submissions: 852.1K
# Testcase Example:  '[]\nno cycle'
#
#
# Given a linked list, determine if it has a cycle in it.
#
#
#
# Follow up:
# Can you solve it without using extra space?
#
#
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        nodeSeen = set()
        while head != None:
            if head not in nodeSeen:
                nodeSeen.add(head)
                head = head.next
            else:
                return True
        return False
