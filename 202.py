class Solution(object):
    def CandD(self, n):
        s = 0
        for i in str(n):
            s += pow(int(i), 2)
        return s

    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        result_set = []
        while n != 1:
            if n not in result_set:
                result_set.append(n)
            else:
                return False
            n = self.CandD(n)
        return True


if __name__ == '__main__':
    print Solution().isHappy(2)
