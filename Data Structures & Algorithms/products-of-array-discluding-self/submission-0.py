class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        master = 1
        c = 0
        for i in range (len(nums)):
            if nums[i] == 0 and c==0:
                c += 1
                continue
            if nums[i] == 0 and c ==1:
                c += 1
                break
            master *= nums[i]
        res = []
        for i in range (len(nums)):
            if c==0:
                res.append(master//nums[i])
            if c == 1:
                if nums[i]!=0:
                    res.append(0)
                else:
                    res.append(master)
            if c == 2:
                res = [0]*len(nums)
                break
        return res