# A city's skyline is the outer contour of the silhouette formed by all the buildings in that city when viewed from a distance. Given the locations and heights of all the buildings, return the skyline formed by these buildings collectively.
#
# The geometric information of each building is given in the array buildings where buildings[i] = [lefti, righti, heighti]:
#
#     lefti is the x coordinate of the left edge of the ith building.
#     righti is the x coordinate of the right edge of the ith building.
#     heighti is the height of the ith building.
#
# You may assume all buildings are perfect rectangles grounded on an absolutely flat surface at height 0.
#
# The skyline should be represented as a list of "key points" sorted by their x-coordinate in the form [[x1,y1],[x2,y2],...]. Each key point is the left endpoint of some horizontal segment in the skyline except the last point in the list, which always has a y-coordinate 0 and is used to mark the skyline's termination where the rightmost building ends. Any ground between the leftmost and rightmost buildings should be part of the skyline's contour.
#
# Note: There must be no consecutive horizontal lines of equal height in the output skyline. For instance, [...,[2 3],[4 5],[7 5],[11 5],[12 7],...] is not acceptable; the three lines of height 5 should be merged into one in the final output as such: [...,[2 3],[4 5],[12 7],...]
from typing import *
from heapq import *


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        def ridx(buildings):
            return (-buildings[2], buildings[0], buildings[1])

        L = list(set([_[0] for _ in buildings] + [_[1] for _ in buildings]))
        L.sort()
        buildings_idx = 0
        heap = []
        result = []
        crt_height = -1
        for x in L:
            while buildings_idx < len(buildings) and buildings[buildings_idx][0] <= x:
                heappush(heap, ridx(buildings[buildings_idx]))
                buildings_idx += 1
            while len(heap) > 0 and heap[0][2] <= x:
                heappop(heap)
            if len(heap) == 0:
                result.append([x, 0])
                crt_height = 0
            elif crt_height != -heap[0][0]:
                result.append([x, -heap[0][0]])
                crt_height = -heap[0][0]
        return result


A = Solution()

buildings = [[2, 9, 10], [3, 7, 15], [5, 12, 12], [15, 20, 10], [19, 24, 8]]
A.getSkyline(buildings=buildings)