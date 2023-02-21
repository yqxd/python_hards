"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.



Example 1:

Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:

Input: nums = [1], k = 1
Output: [1]
"""

from typing import *
from collections import defaultdict
from heapq import *

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        result = []
        D = defaultdict(int)
        H = []
        for _ in range(k):
            heappush(H, -nums[_])
            D[-nums[_]] += 1
        for _ in range(k, len(nums)):
            while D[H[0]] == 0:
                heappop(H)
            result.append(-H[0])
            D[-nums[_ - k]] -= 1
            D[-nums[_]] += 1
            heappush(H, -nums[_])
        while D[H[0]] == 0:
            heappop(H)
        result.append(-H[0])
        return result


nums = [1, 3, -1, -3, 5, 3, 6, 7]
k = 3
A = Solution()
A.maxSlidingWindow(nums, k)
