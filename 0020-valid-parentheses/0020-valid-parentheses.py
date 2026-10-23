class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        group = {")": "(", "]": "[", "}": "{"}
        stack = []
        for ch in s:
            if ch in group:
                if not stack or stack.pop() != group[ch]:
                    return False
            else:
                stack.append(ch)
        return not stack