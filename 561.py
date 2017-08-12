class Solution(object):
    def arrayPairSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        ''' Time Limit Exceeded
        new = 0
        for i in xrange(0, len(nums)):
            for j in xrange(0, len(nums)-i-1):
                if nums[j] > nums[j+1]:
                    tmp = nums[j+1]
                    nums[j+1] = nums[j]
                    nums[j] = tmp
        for i in xrange(0, len(nums), 2):
            new = new + nums[i]
        return new
        '''
        nums.sort()
        new = 0
        for i in xrange(0, len(nums), 2):
            new = new + nums[i]
        return new


if __name__ == '__main__':
    print Solution().arrayPairSum([7,3,1,0,0,6])