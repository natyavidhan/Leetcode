class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        copy = nums.copy()
        x = 0
        for idx, i in enumerate(copy):
            if i == val:
                nums.pop(idx-x)              
                x+=1
        return len(nums)
        