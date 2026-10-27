class Solution:
    def isPalindrome(self, s: str) -> bool:
        char = []
        for c in s:
            if c.isalnum():
                c = c.lower()
                char.append(c) 

        length = len(char)
        last = length
        i = 0
        while i < length/2:
            if char[i] == char[last - 1]:
                i+=1
                last-=1
            else:
                return False
            
        return True