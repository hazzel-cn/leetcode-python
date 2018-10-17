class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        i = 1
        j = 0
        jcount = 0

        for i in range(1, len(nums)):
            if nums[j] == nums[i]:
                jcount += 1
                if jcount < 2:
                    nums[j+1] = nums[i]
                    j += 1
            else:
                nums[j+1] = nums[i]
                jcount = 0
                j += 1
        return j + 1
