class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
<<<<<<< HEAD
        valuelist = []
        resultlist = []

        for i in range(0, nums):
            if nums[i] in valuelist:
                continue
            else:
                valuelist.append(nums[i])
=======
        if len(nums) < 3:
            return []

        rlist = []
        nums.sort()

        for i in range(0, len(nums) - 2):
            # To skip reduncant First Number
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if nums[i] + nums[left] + nums[right] == 0:
                    rlist.append([nums[i], nums[left], nums[right]])
                    left += 1
                    right -= 1
                    # then to skip redundant situations
                    while left < right and nums[left-1] == nums[left]:
                        left += 1
                    while left < right and nums[right+1] == nums[right]:
                        right -= 1
                elif nums[i] + nums[left] + nums[right] < 0:
                    left += 1
                elif nums[i] + nums[left] + nums[right] > 0:
                    right -= 1
        return rlist



if __name__ == '__main__':
    print Solution().threeSum([-1, 0, 1, 2, -1, -4])

>>>>>>> 96929d35477369abb47e0a51df35e28e5473f25d
            