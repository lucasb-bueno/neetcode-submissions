class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hmap = {
            "}":"{",
            "]":"[",
            ")":"("
        }
       
        for char in s:
            if char not in hmap:
                stack.append(char)
                continue
            if not stack or stack[-1] != hmap[char]:
                return False
            stack.pop()
        return not stack
            
        
