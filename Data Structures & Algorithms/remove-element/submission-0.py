class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        idxToSet = 0
        for num in nums:
            if num == val:
                continue
            nums[idxToSet] = num
            idxToSet += 1
        return idxToSet