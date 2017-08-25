class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.append(9999)
        if target <= nums[0]:
            return 0
        for i in range(1, len(nums)):
            if nums[i-1] < target <= nums[i]:
                return i


if __name__ == '__main__':
    print Solution().searchInsert([1,3,5,6], 0)
