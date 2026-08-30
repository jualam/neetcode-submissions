class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        l=0
        store=set()
        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            store.add(s[r])
            maxlen=max(maxlen,len(store))

        return maxlen
            
