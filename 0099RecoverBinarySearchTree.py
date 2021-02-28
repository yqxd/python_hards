"""
You are given the root of a binary search tree (BST), where exactly two nodes of the tree were swapped by mistake. Recover the tree without changing its structure.

Follow up: A solution using O(n) space is pretty straight forward. Could you devise a constant space solution?



Example 1:


Input: root = [1,3,null,null,2]
Output: [3,1,null,null,2]
Explanation: 3 cannot be a left child of 1 because 3 > 1. Swapping 1 and 3 makes the BST valid.
Example 2:


Input: root = [3,1,4,null,null,2]
Output: [2,1,4,null,null,3]
Explanation: 2 cannot be in the right subtree of 3 because 2 < 3. Swapping 2 and 3 makes the BST valid.


Constraints:

The number of nodes in the tree is in the range [2, 1000].
-231 <= Node.val <= 231 - 1
"""


# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: None Do not return anything, modify root in-place instead.
        """
        num = []
        cur = root
        self.add(num, cur)
        for i in range(1, len(num)):
            if num[i-1].val > num[i].val:
                for j in range(i, 0, -1):
                    if num[j-1].val > num[j].val:
                        num[j - 1].val, num[j].val = num[j].val, num[j - 1].val
                    else:
                        break

    def add(self, num, cur):
        if cur is None:
            return
        else:
            self.add(num, cur.left)
            num.append(cur)
            self.add(num, cur.right)

a1 = TreeNode(1)
a2 = TreeNode(2)
a3 = TreeNode(3)
a4 = TreeNode(4)
a5 = TreeNode(5)
a3.left = a1
a1.right = a2
a3.right = a5
a5.left = a4

a3.val, a5.val = a5.val, a3.val
A = Solution()
A.recoverTree(a3)