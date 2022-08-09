class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected = [i for i in range(1, len(nums)+1)]
        for num in expected:
            if num not in nums:
                return num
        return 0