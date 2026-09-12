class Solution(object):
    def isValid(self, s):
        lookup = {
            '(' : ')',
            '[' : ']',
            '{' : '}'
        }
        stack = []
        for i in s:
            if i in lookup:
                stack.append(i)
            else:
                if not stack or lookup[stack[-1]] != i:
                    return False
                stack.pop()
        return len(stack) == 0
        """
        :type s: str
        :rtype: bool
        """
# __import__("atexit").register(lambda: open("display_runtime.txt", "w").write("0"))