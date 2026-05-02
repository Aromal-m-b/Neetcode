from collections import defaultdict
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = defaultdict(list)
        hashmap[tuple(sorted(t))].append(t)
        hashmap[tuple(sorted(s))].append(s)
        v = hashmap[tuple(sorted(s))]
        if len(v) == 2:
            return True
        else:
            return False