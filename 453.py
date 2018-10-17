class Solution(object):
    def minMoves(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        base = min(nums)
        for i in nums:
            count += i - base
        return count

if __name__ == '__main__':
    print Solution().minMoves([1,2,5])