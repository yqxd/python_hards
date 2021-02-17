"""
You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.



Example 1:

Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6
Example 2:

Input: lists = []
Output: []
Example 3:

Input: lists = [[]]
Output: []


Constraints:

k == lists.length
0 <= k <= 10^4
0 <= lists[i].length <= 500
-10^4 <= lists[i][j] <= 10^4
lists[i] is sorted in ascending order.
The sum of lists[i].length won't exceed 10^4.
"""


# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


import heapq


class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        tasks = []
        allnum = len(lists)
        for pos in range(allnum):
            if lists[pos] != None:
                heapq.heappush(tasks, (lists[pos].val, pos))
            else:
                allnum -= 1
        head = ListNode(0)
        now = head
        while allnum != 0:
            _, pos = heapq.heappop(tasks)
            now.next = lists[pos]
            now = now.next
            lists[pos] = lists[pos].next
            if lists[pos] is None:
                allnum -= 1
            else:
                heapq.heappush(tasks, (lists[pos].val, pos))
        return head.next


A = Solution()
a1 = ListNode(1)
a2 = ListNode(2)
a3 = ListNode(3)
a4 = ListNode(4)
a5 = ListNode(5)
a1.next = a3
a3.next = a5
a2.next = a4
result = A.mergeKLists([a1, a2, None])
while result != None:
    print(result.val)
    result = result.next
