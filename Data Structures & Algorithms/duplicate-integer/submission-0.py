from collections import defaultdict
class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        hashmap = defaultdict(list)
        for s in nums:
            hashmap[s].append(s)
        more = False
        for values in hashmap.values():
            if(len(values)>1):
                more = True
                break
            else:
                continue
        return more