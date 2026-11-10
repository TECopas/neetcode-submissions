class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        prospect = 0
        for n in nums:
            if n == 1:
                prospect += 1
            else:
                prospect = 0
            res = max(res, prospect)

        return res