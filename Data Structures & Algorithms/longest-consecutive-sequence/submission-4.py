class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        nums.sort()
        store = set(nums)
        i=0
        for num in nums:
            curr , streak = num ,0
            while curr in store:
                curr += 1
                streak += 1
            res = max(res,streak)
        return res