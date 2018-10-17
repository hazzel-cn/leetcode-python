class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        start = 0
        end = min(len(s), start + k)
        zhz = s[start: end][::-1]

        while start + k < len(s):
            zhz += s[start + k: start + 2 * k]
            start = start + 2 * k
            end = min(len(s), start + k)
            # print start, end
            zhz += s[start: end][::-1]
        return zhz
        # bacdfeg


if __name__ == '__main__':
    print Solution().reverseStr('abcd', 4)
