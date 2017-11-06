class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if len(nums) < 2:
            return nums
        relist = []
        nums.sort()

        


if __name__ == '__main__':
    print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])