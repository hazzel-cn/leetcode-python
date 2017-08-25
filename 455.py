class Solution(object):
    def findContentChildren(self, g, s):
        """
        :type g: List[int]
        :type s: List[int]
        :rtype: int
        """
        s.sort()
        g.sort()
        count = 0
        for i in g:
            for j in s:
                if j >= i:
                    count += 1
                    s.remove(j)
                    break
        return count


if __name__ == '__main__':
    print Solution().findContentChildren([1,2], [1,2,3])