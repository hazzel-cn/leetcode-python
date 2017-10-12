class Solution(object):
    def isPowerOfTwo(self, n):
        """
        :type n: int
        :rtype: bool
        """
        while n > 1:
            n = n / 2.0
        if n != 1:
            return False
        return True