class MedianFinder:

    def __init__(self):

        ## will be defining two heap, small heap ( all elements are less than large heap)

        self.small = [] ## this is max heap
        self.large = [] ## this is min heap
        

    def addNum(self, num: int) -> None:
        ## add any new element to the small heap
        heapq.heappush(self.small, -1*num)

        ## now, after the new insertion. Check if the conditions are met
        ##check1, if element in small heap < elements in large heap

        if self.small and self.large and (-1*self.small[0] > self.large[0]):
            temp1 = -1* heapq.heappop(self.small)
            heapq.heappush(self.large, temp1)
        
        ### ORDER IS IMPORTANT
        ##check2, if the size difference is not greater than 1

        if len(self.small) > len(self.large)+1:
            ## small heap is bigger
            temp = -1*heapq.heappop(self.small)
            heapq.heappush(self.large,temp)
        
        if len(self.large) > len(self.small)+1:
            ## large heap is too big
            temp = heapq.heappop(self.large)
            heapq.heappush(self.small,-temp)
        
        ##check2, if element in small heap < elements in large heap

        if self.small and self.large and (-1*self.small[0] > self.large[0]):
            temp1 = -1* heapq.heappop(self.small)
            heapq.heappush(self.large, temp1)
        

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            ## odd length, which ever has the extra element is the media

            return -1*self.small[0]
        
        if len(self.large)> len(self.small):
            return self.large[0]
        
        return (-1*self.small[0]+self.large[0])/2.0
        
        