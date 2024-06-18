class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = {}
        l = []
        for i in strs:
            s = "".join(sorted(i))
            if  s in d:
                d[s].append(i)
            else:
                d[s] = [i]
        for j in d:
            l.append(d[j])
        return l