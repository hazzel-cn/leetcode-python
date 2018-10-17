class Solution(object):
    def findErrorNums(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        zhz_dict = {}
        re_num = 0
        for i in nums:
            if i not in zhz_dict:
                zhz_dict[i] = 1
            else:
                zhz_dict[i] += 1
                re_num = i
        for i in range(1, len(nums)+1):
            if i not in zhz_dict:
                return [re_num, i]