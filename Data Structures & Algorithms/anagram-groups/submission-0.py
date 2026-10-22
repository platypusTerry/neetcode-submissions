class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        seen = {}
        for word in strs:
            key = "".join(sorted(word)) #把字串排序後黏在一起 #key也是自己取的名字
            if key not in seen: #先把key建立起來
                seen[key] = []
               # ^^^ key ^^ value 
            seen[key].append(word)

        return list(seen.values()) #把東西轉成list
            

