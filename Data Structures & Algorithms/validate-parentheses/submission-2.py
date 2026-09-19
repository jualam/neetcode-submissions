class Solution:
    def isValid(self, s: str) -> bool:
        store=[]
        for i in s:
            if i=='(' or i=='{' or i =='[':
                store.append(i)
            else:
                if not store:
                    return False
                else:
                    if i == ')' and store[-1] == '(':
                        store.pop()
                    elif i == '}' and store[-1] == '{':
                        store.pop()
                    elif i == ']' and store[-1] == '[':
                        store.pop()
                    else:
                        return False
        return not store