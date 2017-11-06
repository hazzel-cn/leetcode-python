class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        nums.sort()
        dval = target - nums[0] - nums[1] - nums[-1]
        rlist = [0, 1, -1]

        for i in range(0, len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            left = i + 1
            right = len(nums) - 1
            while left < right:
                new_dval = target - nums[i] - nums[left] - nums[right]
                if new_dval < 0:
                    if abs(new_dval) <= abs(dval):
                        dval = new_dval
                        rlist = [nums[i], nums[left], nums[right]]
                    right -= 1
                elif new_dval > 0:
                    if abs(new_dval) <= abs(dval):
                        dval = new_dval
                        rlist = [nums[i], nums[left], nums[right]]
                    left += 1
                else:
                    return nums[i] + nums[left] + nums[right]
        return rlist[0] + rlist[1] + rlist[2]


if __name__ == '__main__':
    print Solution().threeSumClosest([-1,2,1,-4],1)

