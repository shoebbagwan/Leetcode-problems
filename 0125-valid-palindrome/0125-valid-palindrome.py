class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        cleaned = [c.lower() for c in s if c.isalnum()]
        return cleaned == cleaned[::-1]
        