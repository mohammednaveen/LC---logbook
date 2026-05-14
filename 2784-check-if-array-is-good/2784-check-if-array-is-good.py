class Solution:
    def isGood(self, nums: list[int]) -> bool:
        n = len(nums) - 1
        
        # Guard clause: base[n] requires at least two elements [1, 1]
        if n < 1:
            return False
            
        # Frequency array to store counts of each number
        # We only care about numbers up to n
        counts = [0] * (n + 1)
        
        for x in nums:
            # If any number is greater than n, it can't be base[n]
            if x > n:
                return False
            counts[x] += 1
            
        # Check counts for 1 to n-1 (must be 1)
        for i in range(1, n):
            if counts[i] != 1:
                return False
        
        # Check count for n (must be 2)
        return counts[n] == 2