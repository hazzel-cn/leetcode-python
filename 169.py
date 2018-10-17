class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zhz = {}
        for i in nums:
            if i in zhz:
                zhz[i] += 1
            else:
                zhz[i] = 1
        control_line = len(nums) / 2
        # print 'Line =', control_line
        for i in zhz:
            print i, zhz[i]
            if zhz[i] > control_line:
                return i


if __name__ == '__main__':
    print Solution().majorityElement([1,3,5,6,1])