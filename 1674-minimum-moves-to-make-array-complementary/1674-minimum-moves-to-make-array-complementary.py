class Solution:
    def minMoves(self, nums: List[int], k: int) -> int:
        # diff[s] stores the change in moves needed for target sum s
        diff = [0] * (2 * k + 2)
        n = len(nums)
        
        for i in range(n // 2):
            a, b = nums[i], nums[n - 1 - i]
            
            # 1. Default: 2 moves for all sums in [2, 2k]
            diff[2] += 2
            diff[2 * k + 1] -= 2
            
            # 2. Discount to 1 move for sums in [min(a,b)+1, max(a,b)+k]
            diff[min(a, b) + 1] -= 1
            diff[max(a, b) + k + 1] += 1
            
            # 3. Discount to 0 moves for exactly a + b
            diff[a + b] -= 1
            diff[a + b + 1] += 1
            
        # Sweep line to find the minimum moves
        ans = n
        current_moves = 0
        for s in range(2, 2 * k + 1):
            current_moves += diff[s]
            ans = min(ans, current_moves)
            
        return ans