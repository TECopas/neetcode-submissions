class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def bsearch(l, r):

            #base case failure condition
            if l > r:
                return -1

            #base case success condition
            m = ((r-l)//2)+l
            if nums[m]==target:
                return m
            
            #recursion conditions
            if target > nums[m]:
                return bsearch(m+1, r)
            else:
                return bsearch(l, m-1)
            

        return bsearch(0, len(nums)-1)

            