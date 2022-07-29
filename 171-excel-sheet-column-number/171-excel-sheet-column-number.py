class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        result = 0;
        for B in range(len(columnTitle)):
            result *= 26;
            result += ord(columnTitle[B]) - ord('A') + 1;
        return result;