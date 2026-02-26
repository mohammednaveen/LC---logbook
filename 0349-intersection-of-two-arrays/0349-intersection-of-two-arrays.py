class Solution(object):
    def intersection(self, nums1, nums2):
        seen = set(nums1)
        res = []
        for i in nums2:
            if i in seen and i not in res:
                res.append(i)
            else:
                continue
        return res
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

"""
seen = set(nums1)
res = []
for i in nums2:
    if i in seen:
        res.append(i)
        seen.remove(i)
return res
"""