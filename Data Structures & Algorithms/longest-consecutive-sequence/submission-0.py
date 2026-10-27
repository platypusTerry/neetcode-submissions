class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        s = set(nums) #把list轉成set
        answer= 1
        if not nums: #針對空陣列
            return 0
        for x in s:
            cur = 1
            if x-1 in s:
                continue #跳下一個for
            index = x + 1
            while index in s: 
# 不知道while能不能這樣寫，還有這樣不就等於兩個回圈了嗎？怎麼會是O(n)，萬一今天是9,8,7,6,5,4,3,,2,1,20,19,18,17,15,14,13, 12,11，那這樣for 會到1,11,17才開始進行while，然後while又從1跑到9，所以這樣應該怎麼算時間複雜度，頂多是很多個n嗎？不會到n個n，所以可以說是O(n)嗎?
                index += 1
                cur += 1
                answer = max(answer, cur)
        return answer