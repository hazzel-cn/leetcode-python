class Solution(object):
    def maxCount(self, m, n, ops):
        """
        :type m: int
        :type n: int
        :type ops: List[List[int]]
        :rtype: int
        """
        min_0 = m
        min_1 = n
        for a, b in ops:
            min_0 = min(min_0, a)
            min_1 = min(min_1, b)
        return min_0 * min_1


if __name__ == '__main__':
    print Solution().maxCount(39999, 39999, [[19999,19999]])