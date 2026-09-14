class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        max_length = 0
        start = 0
        for stop in range(len(s)):
            while s[stop] in seen:
                seen.remove(s[start])
                start += 1
            seen.add(s[stop])
            max_length = max(max_length,stop-start+1)
        return max_length

# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))