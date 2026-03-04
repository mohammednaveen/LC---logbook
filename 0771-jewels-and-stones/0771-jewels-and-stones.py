class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        count = 0
        jewels = set(jewels)
        for ch in stones:
            if ch in jewels:
                count += 1
        return count