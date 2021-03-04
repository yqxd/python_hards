"""
Given an unsorted array, find the maximum difference between the successive elements in its sorted form.

Return 0 if the array contains less than 2 elements.

Example 1:

Input: [3,6,9,1]
Output: 3
Explanation: The sorted form of the array is [1,3,6,9], either
             (3,6) or (6,9) has the maximum difference 3.
Example 2:

Input: [10]
Output: 0
Explanation: The array contains less than 2 elements, therefore return 0.
Note:

You may assume all elements in the array are non-negative integers and fit in the 32-bit signed integer range.
Try to solve it in linear time/space.
"""


class Solution(object):
    def maximumGap(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l <= 1:
            return 0
        num = nums[0]
        if_all = True
        for i in nums:
            if i != num:
                if_all = False
                break
        if if_all:
            return 0
        bucks = [[] for _ in nums]
        M, m = max(nums) + 1, min(nums)
        B = (M - m) / l
        for num in nums:
            bucks[int((num - m) / B)].append(num)
        inde1 = 0
        M = 0
        while True:
            index2 = inde1 + 1
            if index2 >= len(bucks):
                return M
            while not bucks[index2]:
                index2 += 1
                if index2 >= len(bucks):
                    return M
            M = max(M, min(bucks[index2]) - max(bucks[inde1]))
            inde1 = index2


A = Solution()
print(A.maximumGap([1, 1, 1, 1]))
