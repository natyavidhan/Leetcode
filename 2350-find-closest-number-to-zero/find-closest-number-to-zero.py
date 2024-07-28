class Solution:
    def findClosestNumber(self, nums: List[int]) -> int:
        def mod(x):
            return -x if x < 0 else x
        closest = nums[0]
        for n in nums:
            _n = mod(n)
            _closest = mod(closest)
            if _n < _closest or ((_n == _closest) and (n > closest)):
                closest = n
        return closest