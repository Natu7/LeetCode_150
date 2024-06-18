class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
       ## nums_set = set(nums)
        d = {}
        for i in nums:
            d[i] = d.get(i,0) + 1
        print(d)
        d_sorted = dict( sorted(d.items(), key=operator.itemgetter(1),  reverse=True))
        l = list(d_sorted.keys())
        return l[:k]
