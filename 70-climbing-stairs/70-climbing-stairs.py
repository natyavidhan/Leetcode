class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1 or n == 2:
            return n
        last2 = 1
        last = 2
        current = 0
        for step in range(3, n+1):
            current = last2 + last
            last2 = last
            last = current
        return current