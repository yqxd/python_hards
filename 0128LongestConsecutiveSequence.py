"""
Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.



Example 1:

Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.
Example 2:

Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9


Constraints:

0 <= nums.length <= 104
-109 <= nums[i] <= 109
"""


class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        dict = {}
        M = 1
        for num in nums:
            if num not in dict:
                dict[num] = 1
                if num + 1 in dict and num - 1 in dict:
                    N = dict[num - dict[num - 1]] + dict[num + dict[num + 1]] + 1
                    dict[num - dict[num - 1]] = N
                    dict[num + dict[num + 1]] = N
                    if N > M:
                        M = N
                elif num + 1 in dict:
                    dict[num], dict[num + dict[num + 1]] = dict[num] + dict[num + dict[num + 1]], dict[num] + dict[
                        num + dict[num + 1]]
                    if dict[num] > M:
                        M = dict[num]
                elif num - 1 in dict:
                    dict[num], dict[num - dict[num - 1]] = dict[num] + dict[num - dict[num - 1]], dict[num] + dict[
                        num - dict[num - 1]]
                    if dict[num] > M:
                        M = dict[num]

        return M


A = Solution()
print(A.longestConsecutive([100,4,200,1,3,2]))
