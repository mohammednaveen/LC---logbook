class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = dict()
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment not in seen:
                seen[num] = i
            else:
                return [i,seen[compliment]]