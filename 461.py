class Solution(object):
    def hammingDistance(self, x, y):
        """
        :type x: int
        :type y: int
        :rtype: int
        """
        return bin(x^y).count('1')
        
if __name__ == '__main__':
    x = 4
    y = 1
    print Solution().hammingDistance(x, y)