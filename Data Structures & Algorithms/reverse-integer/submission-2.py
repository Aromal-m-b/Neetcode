class Solution:
    def reverse(self, x: int) -> int:
        num = x
        res  = str(abs(int(x)))
        val = int(res[::-1])
        if num < 0:
            val*=-1
        if val < -(1<<31) or val > ((1<<31)-1):
            return 0
        return val
        