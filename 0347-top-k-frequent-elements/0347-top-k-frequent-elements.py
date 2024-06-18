class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_set = set(nums)
        d = {}
        print(nums_set)
        for i in nums_set:
            d[i] = nums.count(i)
        d_sorted = dict( sorted(d.items(), key=operator.itemgetter(1),  reverse=True))
        l = list(d_sorted.keys())
        return l[0:k]
