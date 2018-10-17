class Solution(object):
    def constructRectangle(self, area):
        """
        :type area: int
        :rtype: List[int]
        """
        W = 1
        zhz = [area, 1]
        while W * W <= area :
            L = area / W
            if L * W == area and L >= W:
                # Success
                if L - W < zhz[0] - zhz[1]:
                    zhz = [L, W]
            else:
                # Fail
                pass
            W += 1
        return zhz


if __name__ == '__main__':
    print Solution().constructRectangle(4)