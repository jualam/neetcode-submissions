class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        h_freq=0
        res=0
        store={}
        l=0
        for r in range(len(s)):
            store[s[r]]=store.get(s[r],0)+1
            h_freq=max(h_freq,store[s[r]])
            while (r-l+1)-h_freq>k:
                store[s[l]]-=1
                l+=1
            res=max(res,r-l+1)
        return res
