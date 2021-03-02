"""
Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane, return the maximum number of points that lie on the same straight line.



Example 1:


Input: points = [[1,1],[2,2],[3,3]]
Output: 3
Example 2:


Input: points = [[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]
Output: 4


Constraints:

1 <= points.length <= 300
points[i].length == 2
-104 <= xi, yi <= 104
All the points are unique.
"""

from collections import defaultdict


class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        if len(points) <= 2:
            return len(points)
        M = 1
        d = defaultdict(int)
        for i in range(len(points) - 1):
            d.clear()
            for j in range(i + 1, len(points)):
                d[self.k(points[i], points[j])] += 1
            M = max(max(d.values()), M)
        return M + 1

    def k(self, x, y):
        if x[0] == y[0]:
            return float("Inf")
        else:
            return (y[1] - x[1]) / (y[0] - x[0])


A = Solution()
print(A.maxPoints([[0, 0], [4, 5], [7, 8], [8, 9], [5, 6], [3, 4], [1, 1]]))
