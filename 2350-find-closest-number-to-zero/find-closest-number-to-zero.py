class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        def mod(x):
            return -x if x < 0 else x
        closest = nums[0]
        for n in nums:
            if mod(n) < mod(closest):
                closest = n
            elif mod(n) == mod(closest):
                if n > closest:
                    closest = n
        return closest