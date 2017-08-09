class Solution(object):
    def matrixReshape(self, nums, r, c):
        """
        :type nums: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        count = 0
        allelement = list()
        for i in nums:
            for j in i:
                count = count + 1
                allelement.append(j)
        if count != r * c:
            return nums
        else:
            result = list()
            while len(allelement) > c-1:
                row_tmp = list()
                for i in xrange(c):
                    row_tmp.append(allelement[0])
                    allelement.pop(0)
                result.append(row_tmp)
            if len(allelement) > 0:
                result.append(allelement)
            return result




        

if __name__ == '__main__':
    print Solution().matrixReshape([[1,2],[3,4]], 4, 1)