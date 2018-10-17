class Solution(object):
    def findLengthOfLCIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0

        max_count = 1
        tmp_max_count = 1

        for i in range(0, len(nums)-1):
            if nums[i] < nums[i+1]:
                tmp_max_count += 1
            else:
                max_count = max(max_count, tmp_max_count)
                tmp_max_count = 1
            max_count = max(max_count, tmp_max_count)
        return max_count


if __name__ == '__main__':
    print Solution().findLengthOfLCIS([1])