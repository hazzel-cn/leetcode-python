class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        # for i in range(1, len(nums)+1):
        #     while nums[i] != i:
        #         print(i, nums[i], nums[nums[i]])
        #         if nums[i] != nums[nums[i]]:
        #             tag = nums[i]
        #             nums[i], nums[tag] = nums[tag], nums[i]
        #         else:
        #             break
        # res = []
        # for i in range(1, len(nums)+1):
        #     if nums[i] != i:
        #         res.append(nums[i])
        # return res
        return list(set(range(1, len(nums)+1)) - set(nums))


n = [0,1,3,4,1,2]
print(Solution().findDisappearedNumbers(n))
