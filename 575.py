class Solution(object):
    def distributeCandies(self, candies):
        """
        :type candies: List[int]
        :rtype: int
        """
        candies_can = {}
        can_get = len(candies) / 2
        for item in candies:
            if item not in candies_can:
                candies_can[item] = 1
            else:
                candies_can[item] = candies_can[item] + 1
        return min(can_get, len(candies_can))


if __name__ == '__main__':
    print Solution().distributeCandies([1,1,2,3])