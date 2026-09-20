class Solution:
    def isValid(self, s: str) -> bool:
        dict={')':'(',']':'[','}':'{'}
        stack=[]
        for i in s:
            if i=='(' or i=='{' or i=='[':
                stack.append(i)
            else:
                if stack and stack[-1]==dict[i]:
                    stack.pop()
                else:
                    return False
        return True if not stack else False

