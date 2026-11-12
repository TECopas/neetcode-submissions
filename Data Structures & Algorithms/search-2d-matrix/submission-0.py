class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #find the appropriate row of matrix[i], then find col matrix[i][j]
        #bs on the rows to find the closest, and then bs on that row itself?


        #helper function binary search on inner row
        def bs(x, l, r):
            #failure base case:
            if l>r:
                return False
            #success base case:    
            m = ((r-l)//2)+l
            if matrix[x][m] == target:
                return True

            #recursion cases:
            if target > matrix[x][m]:
                #left moves right
                return bs(x, m+1, r)
            else:
                #right moves left
                return bs(x, l, m-1)

        #find closest approximation of target in range
        u, d, = 0, len(matrix)-1
        while u <= d:
            m = ((d-u)//2)+u
            
            #success condition, we found the appropriate range, run bs
            if matrix[m][0] <= target and  target <= matrix[m][-1]:
                return bs(m, 0, len(matrix[m])-1)
            #first instance of matrix is greater, move d up
            if matrix[m][0] > target:
                d = m - 1
            #last instance of matrix is lesser, move u down
            if matrix[m][-1] < target:
                u = m + 1

        #exit out
        return False