class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """
        C_c = 0
        c_c = len(word)
        for i in word:
            if ord(i) < 91:
                C_c = C_c + 1
        if C_c == 0 or C_c == c_c or (C_c == 1 and ord(word[0]) < 91):
            return True
        else:
            return False


if __name__ == '__main__':
    print Solution().detectCapitalUse('USA')