class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        ans = []
        for idx, i in enumerate(nums):
            total = 0
            for i in range(idx+1):
                total+=nums[i]
            ans.append(total)
        return ans