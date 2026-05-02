class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for val in strs:
            size = str(len(val))
            res = res+size+"#"+val
        return res
    def decode(self, s: str) -> List[str]:
        res = []
        val=i=j=0
        while i < len(s):
            j = i
            while s[j]!="#":
                j+=1
            size = int(s[i:j])
            res.append(s[j+1:j+size+1])
            i = j + 1 + size
        return res