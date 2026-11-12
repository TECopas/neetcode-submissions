class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #upper bound for k is the size of the largest pile
        #need a helper function to determine if a given value of k meets the time limit
        #from there, we search through the range 1...k until we find the minimum using bsearch

        def helper(g):
            hours = h
            pc = piles.copy()
            for p in pc:
                hours -= math.ceil(p/g)
            return hours >= 0

        #keep track of the lowest possible rate
        curLowest = max(piles)
        
        #bsearch through options
        l, r = 1, curLowest
        while l <= r:
            g = ((r-l)//2)+l

            #helper returns true, see if we can optimize lower 
            if helper(g):
                curLowest = g
                r = g - 1
            else:
                #helper returns false, we need to raise the rate
                l = g + 1
        return curLowest






