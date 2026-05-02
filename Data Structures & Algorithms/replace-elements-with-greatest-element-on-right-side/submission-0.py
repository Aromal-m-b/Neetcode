class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        s =  len(arr)
        ans = []
        for i in range(0,s-1):
            ans.append(max(arr[i+1:]))
        ans.append(-1)
        return ans