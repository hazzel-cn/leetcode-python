class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums.sort()
        for i in range(0, len(nums)):
            if i != nums[i]:
                return i
        return len(nums)


if __name__ == '__main__':
    print Solution().missingNumber([0,1,3])