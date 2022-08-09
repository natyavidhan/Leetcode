class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        possible = 0
        for idx, num in enumerate(nums):
            if num == target:
                return idx
            if num < target:
                possible = idx+1
        return possible