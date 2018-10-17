class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        valuelist = []
        resultlist = []

        for i in range(0, nums):
            if nums[i] in valuelist:
                continue
            else:
                valuelist.append(nums[i])
            