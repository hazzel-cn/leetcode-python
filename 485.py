class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max1s = 0
        tmp1s = 0
        for i in nums:
            if i == 0:
                tmp1s = 0
            else:
                tmp1s = tmp1s + 1
            if tmp1s > max1s:
                max1s = tmp1s
        return max1s


if __name__ == '__main__':
    print Solution().findMaxConsecutiveOnes([1,1,0,1,1,1])