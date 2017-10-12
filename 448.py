class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        ret_list = []
        nums.sort()
        for i in range(1, len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                if nums[i]+1 not in ret_list:
                    if nums[i] + 1 not 
                    ret_list.append(nums[i]+1)
        return ret_list


if __name__ == '__main__':
    print Solution().findDisappearedNumbers([4,3,2,7,8,2,3,1])