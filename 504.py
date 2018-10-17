class Solution(object):
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        num_a = num
        zhz = ''
        flag_over_zero = True

        if num < 0:
            flag_over_zero = False
            num_a = -num
        while num_a >= 7:
            zhz = str(num_a % 7) + zhz
            num_a = num_a / 7
        if flag_over_zero:
            return str(num_a) + zhz
        else:
            return '-' + str(num_a) + zhz


if __name__ == '__main__':
    print Solution().convertToBase7(-7)


