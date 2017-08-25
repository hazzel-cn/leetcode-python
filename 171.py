class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # A 65 Z 90
        zhz = 0
        base = 1
        for i in range(len(s)-1, -1, -1):
            zhz += (ord(s[i]) - 64) * base
            base *= 26
        return zhz


if __name__ == '__main__':
    print Solution().titleToNumber('ABB')