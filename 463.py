class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        grid_length = len(grid)
        grid_width = len(grid[0])

        total_length = 0

        for i in range(0, grid_length):
            for j in range(0, grid_width):
                if grid[i][j] == 1:
                    # right
                    if i-1 < 0 or grid[i-1][j] == 0:
                        total_length += 1
                    # left
                    if i+1 > grid_length-1 or grid[i+1][j] == 0:
                        total_length += 1
                    # up
                    if j-1 < 0 or grid[i][j-1] == 0:
                        total_length += 1
                    # down
                    if j+1 > grid_width-1 or grid[i][j+1] == 0:
                        total_length += 1
        return total_length


if __name__ == '__main__':
    g = [[0,1,0,0],
         [1,1,1,0],
         [0,1,0,0],
         [1,1,0,0]]
    print Solution().islandPerimeter(g)