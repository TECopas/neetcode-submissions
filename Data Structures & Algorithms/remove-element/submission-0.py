class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0
        #count out k
        for n in nums:
            if n != val:
                k+=1
        #swap out val in the initial k slots
        for i in range(k):
            if nums[i] == val:
                for j in range(i+1,len(nums)):
                    if nums[j] != val:
                        temp = nums[i]
                        nums[i] = nums[j]
                        nums[j] = temp
                        break
        return k