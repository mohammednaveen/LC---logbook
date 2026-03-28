class Solution(object):
    def strStr(self, haystack, needle):
        # One liner
        # return haystack.find(needle)
        
        j = len(needle)
        z = len(haystack)
        for i in range(len(haystack) - j + 1):
            if (str(haystack[i:i+j]) == str(needle)):
                return i

        else:
            return -1 
        
        
        # My Approach using two pointers
        # for i,ch in enumerate(haystack):
        #     if ch == needle[0]:
        #         length = 1
        #         i += 1
        #         while i < len(haystack) and length < len(needle):
        #             if haystack[i] != needle[length]:
        #                 break
        #             length += 1
        #             i += 1
        #         if length == len(needle):
        #             return i-length
        # return -1
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """