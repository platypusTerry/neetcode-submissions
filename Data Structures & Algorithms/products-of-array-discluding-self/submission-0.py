class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        left = [1] * n #假設所有起始都是1
        right = [1] * n #假設所有起始都是1

        for i in range(1, n):
            left[i] = left[i - 1] * nums[i - 1]
        for i in range(n-2, -1, -1):
            right[i] = right[i + 1] * nums[i + 1]
        
        answer = []
        for i in range(n):
            answer.append(left[i] * right[i])
            #不可用answer[i] = left[i] * right[i]，因為answer是空的
            #要用這樣寫就要answer = [1] * n 先去宣告填東西進去 
        
        return answer