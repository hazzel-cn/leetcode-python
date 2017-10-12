class Solution(object):
    def isPowerOfFour(self, num):
        """
        :type num: int
        :rtype: bool
        """
        while num > 1:
            num = num / 4.0
        if num != 1:
            return False
        return True