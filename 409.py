class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        # "abccccdd"

        zhz_dict = {}
        zhz_len = 0
        odd_flag = 0
        for i in s:
            if i not in zhz_dict:
                zhz_dict[i] = 1
            else:
                zhz_dict[i] += 1

        for i in zhz_dict:
            if zhz_dict[i] / 2 * 2 == zhz_dict[i]:
                zhz_len += zhz_dict[i]
            else:
                zhz_len += zhz_dict[i] - 1
                odd_flag = 1
        zhz_len += 1 if odd_flag == 1 else 0
        return zhz_len


if __name__ == '__main__':
    print Solution().longestPalindrome('bb')