class Solution:
    def isPalindrome(self, s: str) -> bool:
        act = ""
        for c in s:
            if c.isalnum():
                act = act+c.lower()
        return act == act[::-1]