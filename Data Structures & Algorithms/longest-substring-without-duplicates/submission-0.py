class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        answer = 0
        dup = set() # 看有沒有出現過的char的set
        for right in range(len(s)):#O(n)
            while s[right] in dup:#amortized下去，每個字就是一次remove，所以是O(1)
                dup.remove(s[left])
                left += 1

            dup.add(s[right])
            answer = max(answer, right - left + 1)
        
        return answer