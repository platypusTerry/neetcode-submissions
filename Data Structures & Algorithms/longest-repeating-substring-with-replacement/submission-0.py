class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        count = {}
        answer = 0
        for right in range(len(s)):
            char = s[right]
            count[char] = count.get(char, 0) + 1
            need = (right - left + 1) - max(count.values())
            #need = (視窗長度) - 字母出現最多者
            while need > k:
                count[s[left]] -= 1
                left += 1
                need = (right - left + 1) - max(count.values())      
            answer = max(answer, right - left + 1)
            
        return answer
            