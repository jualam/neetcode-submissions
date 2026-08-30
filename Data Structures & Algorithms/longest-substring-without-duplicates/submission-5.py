class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        res=0
        for i in range(len(s)):
            store=set()
            for j in range(i, len(s)):
                if s[j] in store:
                    break
                else:
                    store.add(s[j])
            res=max(res,len(store))
        return res