class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        store = [[] for _ in range(len(nums) + 1)]
        res=[]
        curr=0
        for num in nums:
            count[num]=count.get(num,0)+1
        for key,value in count.items():
            store[value].append(key)
        for i in range(len(store)-1, 0,-1):
            for num in store[i]:
                res.append(num)
                if len(res)==k:
                    return res