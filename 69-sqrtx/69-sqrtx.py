class Solution:
    def mySqrt(self, x: int) -> int:
        if x == 0:
            return 0
        l = x/2.0
        while True:
            g = (l + x/l)/2
            if abs(g - l) < .000001:
                return int(g)
            l = g
        