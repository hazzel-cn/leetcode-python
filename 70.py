class Solution(object):
    def factorial(self, n):
        f = 1
        for i in range(1, n+1):
            f *= i
        return f

    def C(self, m, n):
        return (self.factorial(n) / self.factorial(n-m)) / self.factorial(m)

    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        two_steps_max = n / 2
        sum_value = 0

        for two_count in range(0, two_steps_max+1):
            one_count = n - two_count * 2
            sum_value += self.C(two_count, one_count + two_count)
        return sum_value


if __name__ == '__main__':
    print Solution().climbStairs(1)