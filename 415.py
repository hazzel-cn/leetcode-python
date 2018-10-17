class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = ''
        carry = 0
        max_length = max(len(num1), len(num2))
        re_num1 = num1.zfill(max_length)[::-1]
        re_num2 = num2.zfill(max_length)[::-1]

        for ptr in range(0, max_length):
            tmp_sum = ord(re_num1[ptr]) + ord(re_num2[ptr]) + carry - 96
            ans += str(tmp_sum % 10)
            carry = 1 if tmp_sum > 9 else 0
        ans += str(carry) if carry == 1 else ''
        return ans[::-1]


if __name__ == '__main__':
    print Solution().addStrings('999', '1111')