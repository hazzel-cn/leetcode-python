class Solution(object):
    def __C__(self, n, k):
        def fa(x):
            xf = 1
            for i in range(1, x+1):
                xf *= i
            return xf
        return (fa(n) / fa(n-k)) / fa(k)


    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        anslist = []
        for i in range(0, rowIndex+1):
            item = self.__C__(rowIndex, i)
            anslist.append(item)
        return anslist


if __name__ == '__main__':
    print Solution().getRow(4)