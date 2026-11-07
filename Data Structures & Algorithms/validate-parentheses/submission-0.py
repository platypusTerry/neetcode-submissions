class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        brackets = {")": "(", "]": "[", "}": "{"}

        for c in s:
            if c in brackets: #這樣久能取代很多if了，因為右括是key
                if not stack or stack[-1] != brackets[c]:
                #stack沒東西 右括是第一個東西or頂端的括號對不上對應的左括
                    return False
                else: 
                    stack.pop() #對上左括了直接抵銷
            else: #elif c in "([{":
                stack.append(c)
            
        if not stack:
            return True
        else:
            return False