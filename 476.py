class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        length = len(bin(num)) - 2
        xor = '1'
        while len(xor) < length:
            xor += '1'
        ixor = int(xor, 2)
        return num ^ ixor


if __name__ == '__main__':
    print Solution().findComplement(1)