class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 0:
            return False

        divider_list = []
        import math
        bon = math.sqrt(num)
        for i in range(1, int(bon+1)):
            tmp = num / i
            if i * tmp == num:
                if tmp and i not in divider_list:
                    divider_list.append(i)
                    divider_list.append(tmp)
        while num in divider_list:
            divider_list.remove(num)
        if sum(divider_list) == num:
            return True
        else:
            return False


if __name__ == '__main__':
    print Solution().checkPerfectNumber(1)

