class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        maxLen, currLen = nums[0], nums[0]
        for i, num in enumerate(nums[1:]):
            if num==1:
                currLen += 1
            else:
                currLen = 0
            maxLen = max(maxLen, currLen)
        return maxLen
            