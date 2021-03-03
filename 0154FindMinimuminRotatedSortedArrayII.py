class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <= 2:
            return min(nums)
        else:
            if nums[0] < nums[-1]:
                return nums[0]
            else:
                mid = len(nums) // 2
                if nums[0] > nums[mid]:
                    return self.findMin(nums[0:(mid + 1)])
                elif nums[0] < nums[mid]:
                    return self.findMin(nums[mid::])
                else:
                    return min(self.findMin(nums[mid::]), self.findMin(nums[0:(mid + 1)]))


A = Solution()
print(A.findMin([3,1,3,3]))
