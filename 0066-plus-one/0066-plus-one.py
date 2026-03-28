class Solution(object):
    def plusOne(self, digits):
        digit = int("".join(map(str, digits))) + 1
        res = [int(i) for i in str(digit)]
        return res
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        