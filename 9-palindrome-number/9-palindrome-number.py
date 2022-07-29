class Solution:
    def isPalindrome(self, x: int) -> bool:
        og = str(x)
        reverse = "".join(reversed(str(x)))
        return og == reverse
            