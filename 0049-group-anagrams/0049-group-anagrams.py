class Solution(object):
    def groupAnagrams(self, strs):
        hash_map = {}
        for s in strs:
            key = ''.join(sorted(s))
            hash_map.setdefault(key,[]).append(s)
        return list(hash_map.values())
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        