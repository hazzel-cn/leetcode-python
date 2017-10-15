class Solution(object):
    def readBinaryWatch(self, num):
        """
        :type num: int
        :rtype: List[str]
        """
        zhz = []
        for hour in range(0, 12):
            for minute in range(0, 60):
                hour_bin = bin(hour)
                minute_bin = bin(minute)
                if hour_bin.count('1') + minute_bin.count('1') == num:
                    zhz.append(str(hour)+':'+str(minute).zfill(2))
        return zhz


if __name__ == '__main__':
    print Solution().readBinaryWatch(1)