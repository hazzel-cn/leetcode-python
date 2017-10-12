class Solution(object):
    def containsDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        num_map = {}
        for i in nums:
            if i not in num_map:
                num_map[i] = 1
            else:
                num_map[i] += 1
        for i in num_map:
            if num_map[i] > 1:
                return True
        return False