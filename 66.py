class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        # digit means the single number here.

        base = 0
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            tmp = carry + digits[i]
            carry = 1 if tmp > 9 else 0
            digits[i] = tmp % 10
        if carry == 1:
            digits.insert(0, carry)
        return digits


if __name__ == '__main__':
    print Solution().plusOne([9,9,9,9,9])