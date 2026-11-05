class Solution:
    def minWindow(self, s: str, t: str) -> str:
        need = {}
        window = {}
        missing = len(t)
        answer = []
        left = 0
        best_len = float('inf')
        best_start = 0

        for char in t:
            need[char] = need.get(char, 0) + 1

        for right in range(len(s)):
            #char = s[right]
            window[s[right]] = window.get(s[right], 0) + 1
            if s[right] in need and window[s[right]] <= need[s[right]]:
                missing -= 1
            while missing == 0:
                # 新增：視窗 [left..right] 是湊齊的，先記答案，再縮
                if right - left + 1 < best_len:
                    best_len = right - left + 1
                    best_start = left

                window[s[left]] -= 1
                if s[left] in need and window[s[left]] < need[s[left]]:
                    missing += 1    
                left += 1

             # 新增：從沒湊齊過就回傳空字串
        if best_len == float('inf'):
            return ""
        return s[best_start:best_start + best_len]