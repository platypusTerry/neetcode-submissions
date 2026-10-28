#會不會follow up要我回傳index，那應該就要開dict了吧
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        i = 0
        for i in range(len(nums)): #for i in nums:
            if i > 0 and nums[i]==nums[i-1]:
                continue
            target = -nums[i]
            left = i + 1
            right = len(nums) - 1
            while left < right:
                if target > nums[left]+nums[right]:
                    left += 1
                elif target < nums[left]+nums[right]:
                    right -= 1
                elif target == nums[left]+nums[right]:
                    answer.append([nums[i], nums[left], nums[right]])
                    #因為有在用括號包起來，所以知道是三元組
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left - 1]:#去重，用left, right都可以
                        left += 1

        return answer              