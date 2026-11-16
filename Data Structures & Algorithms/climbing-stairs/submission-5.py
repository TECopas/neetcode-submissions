class Solution:
    def climbStairs(self, n: int) -> int:
        #recurive version
        #they give us the 3 base cases in the example

        #Need to cut down on work by using a dictionary to cache things
        cache = {0:0, 1:1, 2:2, 3:3}

        def recur(n):
            if n <= 0:
                return cache[0]
            if n == 1:
                return cache[1]
            if n == 2: 
                return cache[2]
            if n == 3: 
                return cache[3]

            if n in cache:
                return cache[n]
            else:
                cache[n] = recur(n-1)+recur(n-2)
                return cache[n]


            

        #climbing with 1 step added with climbing with 2 steps
        return recur(n)