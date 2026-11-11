class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        mapping = {}
        for n in nums:
            mapping[n] = mapping.get(n, 0) + 1

        index = 0
        for i in range(0, 3):
            while mapping.get(i, 0) != 0:
                nums[index] = i
                mapping[i] -=1
                index +=1