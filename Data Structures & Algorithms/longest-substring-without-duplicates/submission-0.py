class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        for i in range(len(s)):
            store=set()
            for j in range(i,len(s)):
                if s[j] in store:
                    break
                else:
                    store.add(s[j])
                    maxlen=max(maxlen,len(store))
        return maxlen
            
