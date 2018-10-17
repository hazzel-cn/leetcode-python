class Solution(object):
    def devidePlus(self, num):
        n = 0
        while num > 0:
            n += num % 10
            num = num / 10
        return n

    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            num = self.devidePlus(num)
        return num

