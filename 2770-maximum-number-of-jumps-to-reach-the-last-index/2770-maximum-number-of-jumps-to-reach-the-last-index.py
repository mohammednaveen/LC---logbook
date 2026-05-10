class Solution:
    def maximumJumps(self, nums: List[int], target: int) -> int:
        n = len(nums)
        dp = [-1] * n # each element of this list stores the max steps needed to reach that index 
        dp[0] = 0 # to mark the first element as reachable and all the others are not reachable.

        for j in range(1, n): # traverse from first index
            for i in range(j): # checking individually to ensure the max steps
                if dp[i] != -1 and abs(nums[j] - nums[i]) <= target: 
                    # 1. checks if the element is reachable or not by dp[i] =! -1
                    # 2. checks the condition 
                    dp[j] = max(dp[j], dp[i] + 1) # decides if the current step or the one earlier step was max

        return dp[n-1] # we need the max step to reach the index n-1 as the dp list stores the max steps to reach that specific index we chose dp[n-1].