class Solution(object):
    def __C__(self, n, k):
        def fa(x):
            xf = 1
            for i in range(1, x+1):
                xf *= i
            return xf
        return (fa(n) / fa(n-k)) / fa(k)


    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        trilist = []
        print self.__C__(5,2), self.__C__(5,3)
        for line in range(0, numRows):
            trilist.append([])
            for col in range(0, line):
                element = self.__C__(line, col)
                trilist[line].append(element)
        return trilist


if __name__ == '__main__':
    print Solution().generate(5)