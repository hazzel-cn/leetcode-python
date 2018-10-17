class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        map_t = {}
        map_s = {}

        for i in s:
            if i not in map_s:
                map_s[i] = 1
            else:
                map_s[i] += 1
        for j in t:
            if j not in map_t:
                map_t[j] = 1
            else:
                map_t[j] += 1
        if map_t == map_s:
            return True
        else:
            return False


if __name__ == '__main__':
    print Solution().isAnagram('cat', 'anagrma')