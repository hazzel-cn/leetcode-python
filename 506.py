class Solution(object):
    def findRelativeRanks(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        backup = list(nums)
        nums.sort()
        nums = nums[::-1]

        zhz = {}
        result = []
        for i in range(0, len(nums)):
            zhz[nums[i]] = i # zhz[Score]: Rank
        for i in backup:
            if zhz[i] == 0:
                result.append('Gold Medal')
            elif zhz[i] == 1:
                result.append('Silver Medal')
            elif zhz[i] == 2:
                result.append('Bronze Medal')
            else:
                result.append(str(zhz[i] + 1))
        # print backup
        return result


if __name__ == '__main__':
    print Solution().findRelativeRanks([1])