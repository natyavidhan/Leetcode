class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        letters.sort()
        for i in letters:
            if ord(target) < ord(i):
                return i
        return letters[0]