class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # second approach using len function
        return len(nums)!=len(set(nums))

        # first approach and a proper Hash Table approach used.
        # seen = set()
        # for i in nums:
        #     if i in seen:
        #         return True
        #     else:
        #         seen.add(i)
        # return False