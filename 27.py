class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) < 2:
            return len(nums)
        i = 1
        j = 0
        for i in range(1, len(nums)):
            if nums[i] != nums[j]:
                nums[j+1] = nums[i]
                j += 1
        # print nums
        return j+1


if __name__ == '__main__':
    print Solution().removeElement([3,2,2,3], 3)