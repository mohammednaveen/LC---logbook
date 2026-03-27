class Solution(object):
    def checkPrimeFrequency(self, nums):
        
        def isPrime(num):
            if num < 2:
                return False
            for i in range(2,num):
                if num % i == 0:
                    return False
            return True
        
        seen = set(nums)
        for num in nums:
            if isPrime(nums.count(num)):
                return True
        return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        