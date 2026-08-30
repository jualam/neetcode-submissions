class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        maxlen=0
        store=set()
        l,r=0,0
        for r in range(len(s)):
            while s[r] in store:
                store.remove(s[l])
                l+=1
            store.add(s[r])
            curr_len=len(store)
            maxlen=max(maxlen,curr_len)

        return maxlen

            
