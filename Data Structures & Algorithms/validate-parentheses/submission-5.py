class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        checkClosed = {"}": "{", "]": "[", ")" : "("}
        for c in s:
            if c in checkClosed:
                if stack and stack[-1] == checkClosed[c]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(c)
        
        return True if not stack else False   

        