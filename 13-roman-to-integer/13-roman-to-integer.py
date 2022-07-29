class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        i = 0
        mapped = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000,'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}
        while i < len(s):
            if i+1<len(s) and s[i:i+2] in mapped:
                ans+=mapped[s[i:i+2]]
                i+=2
            else:
                ans+=mapped[s[i]]
                i+=1
        return ans