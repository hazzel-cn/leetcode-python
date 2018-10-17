class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        zhz = 0
        for i in nums:
            zhz = zhz ^ i
        return zhz
        