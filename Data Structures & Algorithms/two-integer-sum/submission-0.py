class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(len(nums)):
            wants = target - nums[i]
            if wants in seen:
                return [seen[wants], i]
            seen[nums[i]] = i
        
        return []

