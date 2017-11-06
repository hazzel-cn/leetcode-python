class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        j = 0
        jcount = 0
        for i in range(1, len(nums)):
            if nums[i] == nums[j]:
                jcount += 1
                # When two elements equal to each other
                # the former one can be replaced only 
                # when in first two rounds. After that, 
                # j should not be changed.
                if jcount < 2:
                    nums[j+1] = nums[i]
                    j += 1
            else:
                nums[j+1] = nums[i]
                jcount = 0
                j += 1

        # print nums
        return j + 1


if __name__ == '__main__':
    print Solution().removeDuplicates([1,1])