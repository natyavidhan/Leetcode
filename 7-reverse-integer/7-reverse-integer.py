class Solution:
    def reverse(self, x: int) -> int:
        neg = x < 0
        s = "".join(reversed(str(x)))
        if neg:
            s=s[:-1]
        ans = -1*int(s) if neg else int(s)
        if ans < -2**31 or ans > 2**31:
            return 0
        return ans
            