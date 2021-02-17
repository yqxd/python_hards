"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes, in the end, should remain as it is.

Follow up:

Could you solve the problem in O(1) extra memory space?
You may not alter the values in the list's nodes, only nodes itself may be changed.


Example 1:


Input: head = [1,2,3,4,5], k = 2
Output: [2,1,4,3,5]
Example 2:


Input: head = [1,2,3,4,5], k = 3
Output: [3,2,1,4,5]
Example 3:

Input: head = [1,2,3,4,5], k = 1
Output: [1,2,3,4,5]
Example 4:

Input: head = [1], k = 1
Output: [1]


Constraints:

The number of nodes in the list is in the range sz.
1 <= sz <= 5000
0 <= Node.val <= 1000
1 <= k <= sz
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        list = []
        while head is not None:
            list.append(head)
            head = head.next
        if len(list) < k or k == 1:
            return list[0]
        n = len(list)
        for i in range(n // k):
            now = i * k
            for j in range(k - 1):
                list[now + j + 1].next = list[now + j]
        for i in range(n // k - 1):
            now = i * k
            list[now].next = list[now + 2 * k - 1]
        list.append(None)
        list[n // k * k - k].next = list[n // k * k]
        return list[k - 1]


A = Solution()
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
result = A.reverseKGroup(a1, 3)
while result != None:
    print(result.val)
    result = result.next
