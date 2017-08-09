class Solution(object):
    def findWords(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        r = list()
        keyboard = ['qwertyuiop','asdfghjkl','zxcvbnm']
        for row in keyboard:
            for a in words:
                if self.check(a.lower(), row):
                    r.append(a)
        print r
        return r

    def check(self, a, b):
        flag = True
        for i in a:
            if i not in b:
                flag = False
        return flag


if __name__ == '__main__':
    so = Solution().findWords(["Hello", "Alaska", "Dad", "Peace"])