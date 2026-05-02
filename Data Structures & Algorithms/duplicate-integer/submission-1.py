class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set(nums)
        return len(nums) != len(test)