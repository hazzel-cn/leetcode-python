class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        h = len(M)      # the range of i is [0, h]
        w = len(M[0])   # the range of j is [0, w]

        new_M = []

        for i in range(0, h):
            line = []
            for j in range(0, w):
                # print 'Origin:', M[i][j]
                neighbor_count = 0
                value_count = 0
                for x in range(i-1, i+2):
                    for y in range(j-1, j+2):
                        if 0 <= x < h and 0 <= y < w:
                            # print M[x][y], x, y
                            neighbor_count += 1
                            value_count += M[x][y]
                # print value_count, neighbor_count
                line.append(value_count / neighbor_count)
            new_M.append((line))    
        return new_M


if __name__ == '__main__':
    print Solution().imageSmoother([[2,3,4],[5,6,7],[8,9,10],[11,12,13],[14,15,16]])
    # [[4,4,5],[5,6,6],[8,9,9],[11,12,12],[13,13,14]]