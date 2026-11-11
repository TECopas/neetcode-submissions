class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #use a max heap, pop items when the heap exceeds k, then return all the items in the end
        maxHeap = []
        heapq.heapify_max(maxHeap)

        for xcoord, ycoord in points:
            dist = xcoord**2 + ycoord**2
            heapq.heappush_max(maxHeap, [dist, xcoord, ycoord])
            if len(maxHeap) > k:
                 heapq.heappop_max(maxHeap)

        res = []
        while maxHeap:
            #unpack the list items from the maxHeap
            dist, xcoord, ycoord = heapq.heappop_max(maxHeap)
            res.append([xcoord, ycoord])
        return res
