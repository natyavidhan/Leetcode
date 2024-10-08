class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(map(bool, nums)):
            return "0"
        nums = list(map(str, nums))
        l = len(nums)
        for x, n in enumerate(nums):
            if l > x+1:
                for y in range(x+1, l):
                    if int(nums[y]+nums[x]) > int(nums[x]+nums[y]):
                        nums[x], nums[y] = nums[y], nums[x]
        return "".join(nums)
