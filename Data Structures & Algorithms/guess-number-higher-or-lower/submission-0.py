# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        l, r = 1, n
        g = ((r-l)//2)+l
        while guess(g) != 0:
            if guess(g) > 0:
                l = g + 1
            if guess(g) < 0:
                r = g - 1
            g = ((r-l)//2)+l

        return g