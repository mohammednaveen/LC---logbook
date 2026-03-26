class Solution(object):
    def containsDuplicate(self, nums):
        unique = set(nums)
        return len(unique) != len(nums)






        # Initial Approach
        # seen = set()
        # for i in nums:
        #     if i not in seen:
        #         seen.add(i)
        #     else:
        #         return True
        # return False
        """
        :type nums: List[int]
        :rtype: bool
        """
        