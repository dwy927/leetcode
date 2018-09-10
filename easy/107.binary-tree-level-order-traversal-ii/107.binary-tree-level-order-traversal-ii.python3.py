#
# [107] Binary Tree Level Order Traversal II
#
# https://leetcode.com/problems/binary-tree-level-order-traversal-ii/description/
#
# algorithms
# Easy (43.37%)
# Total Accepted:    182K
# Total Submissions: 417.2K
# Testcase Example:  '[3,9,20,null,null,15,7]'
#
# Given a binary tree, return the bottom-up level order traversal of its nodes'
# values. (ie, from left to right, level by level from leaf to root).
#
#
# For example:
# Given binary tree [3,9,20,null,null,15,7],
#
# ⁠   3
# ⁠  / \
# ⁠ 9  20
# ⁠   /  \
# ⁠  15   7
#
#
#
# return its bottom-up level order traversal as:
#
# [
# ⁠ [15,7],
# ⁠ [9,20],
# ⁠ [3]
# ]
#
#
#
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        import queue
        if root == None:
            return []

        ret = list()
        q = queue.Queue()
        q.put((root, 0))
        cur = -1
        while not q.empty():
            node, idx = q.get()
            if idx != cur: # 新的一层开始啦
                ret.append([node.val])
                cur = idx
            else:
                ret[idx].append(node.val)
            if node.left:
                q.put((node.left, idx+1))
            if node.right:
                q.put((node.right, idx+1))
        return ret[::-1]
