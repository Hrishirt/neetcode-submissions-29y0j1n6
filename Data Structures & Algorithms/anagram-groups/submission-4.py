class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            skey = sorted(s) 
            skey = "".join(skey)
            if skey in res:
                res[skey].append(s)
            else:
                res[skey] = [s]
        return list(res.values())