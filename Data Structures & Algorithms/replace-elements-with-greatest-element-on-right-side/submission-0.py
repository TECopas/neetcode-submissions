class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        #get all items, switching them out with the max to the right of them
        maxR = arr[-1]
        for i in range(len(arr)-2, -1, -1):
            #temp var to hold the current value in the array in case it is greater than the current maxR
            temp = arr[i]
            #assign the maxR to the right of the current slot
            arr[i] = maxR
            #determine new maxR
            maxR = max(temp, maxR)

        #assign last slot with -1
        arr[-1] = -1

        return arr
            

            
