class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        hmap = defaultdict(int)
        res=[]
        i=0
        for num in nums:
            hmap[num]+=1
        sorted_hmap = dict(sorted(hmap.items(),key = lambda x:x[1],reverse=True))
        freq = list(sorted_hmap.keys())[:k]
        return freq