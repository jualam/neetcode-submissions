class Solution:
    def isValid(self, s: str) -> bool:
        store=[]
        dick={')':'(',']':'[','}':'{'}
        for i in s:
            if i=='(' or i=='{' or i =='[':
                store.append(i)
            else:
                if store and store[-1]==dick[i]:
                    store.pop()
                else:
                    return False
                
        return not store