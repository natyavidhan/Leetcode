class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        if not any(map(bool, nums)):
            return "0"
        nums = [str(i) for i in nums]
        for x, n in enumerate(nums):
            if len(nums) > x+1:
                for y in range(x+1, len(nums)):
                    print(x, y, len(nums))
                    if int(nums[y]+nums[x]) > int(nums[x]+nums[y]):
                        nums[x], nums[y] = nums[y], nums[x]
        return "".join(nums)
