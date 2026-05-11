class Solution:
    def xorOperation(self, n: int, start: int) -> int:
        nums = [0]* n
        res = start
        for i in range(n):
            nums[i] = start + 2 * i
            if i == 0: continue
            res ^= nums[i]
        return res