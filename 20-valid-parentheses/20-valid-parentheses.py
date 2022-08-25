class Solution:
    def isValid(self, s: str) -> bool:
        brackets = ['()', '{}', '[]']
        while any(x in s for x in brackets):
            for br in brackets:
                s = s.replace(br, '')
        return not s