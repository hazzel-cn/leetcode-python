class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        sen_list = s.split(' ')
        new_line = ''
        for word in sen_list:
            new_line  = new_line + ' ' + word[::-1]
        return new_line[1:]

if __name__ == '__main__':
    print Solution().reverseWords("Let's take LeetCode contest")