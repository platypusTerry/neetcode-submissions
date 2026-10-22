class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set();
        for n in nums: #n直接是nums裡面的數字了
            if n in seen:
                return True
            seen.add(n);
        
        return False;


# class Solution:
#     def hasDuplicate(self, nums: List[int]) -> bool:
#         seen = {}
#         for i, n in enumerate(nums): #(i,n)=(0,1), (1,2) (2,3) (3,3)
#             if n in seen:
#                 return True
#             seen[n] = seen.get(n, 0) + 1
                #seen.get(n, 0) 的意思是：n 存在就拿它的值，不存在就當作 0。所以第一次遇到 n 時是 0 + 1 = 1，之後每次再加 1。
        
#         return False