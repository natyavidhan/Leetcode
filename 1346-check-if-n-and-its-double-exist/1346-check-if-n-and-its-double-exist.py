class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for x in arr:
            new = arr.copy()
            new.remove(x)
            for y in new:
                if y*2 == x:
                    return True
        return False