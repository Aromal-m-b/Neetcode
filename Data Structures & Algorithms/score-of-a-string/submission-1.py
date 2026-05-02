class Solution:
    def scoreOfString(self, s: str) -> int:
        ans = []
        for i in range (0,len(s)-1):
            ans.append(abs(ord(s[i+1]) - ord(s[i])))
        return sum(ans)