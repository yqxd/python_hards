"""
Given an unsorted integer array nums, find the smallest missing positive integer.



Example 1:

Input: nums = [1,2,0]
Output: 3
Example 2:

Input: nums = [3,4,-1,1]
Output: 2
Example 3:

Input: nums = [7,8,9,11,12]
Output: 1


Constraints:

0 <= nums.length <= 300
-231 <= nums[i] <= 231 - 1
"""


class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        now = 0
        while now < n:
            if nums[now] == now + 1:
                now += 1
            elif nums[now] > n or nums[now] < 0:
                nums[now] = 0
            else:
                k = nums[now]
                if nums[k - 1] > n or nums[k - 1] <= 0 or nums[k - 1] == k:
                    nums[now], nums[k - 1] = 0, k
                    now += 1
                else:
                    nums[now], nums[k - 1] = nums[k - 1], k
        now = 0
        while now < n:
            if nums[now] == 0:
                return now + 1
            else:
                now += 1
        return n + 1
