class CountSquares:

    def __init__(self):
        self.points = defaultdict(int)
        ## we need to store the points added and also maintain the frequencies
        ## to do this efficiently we use hash map frequencies
        

    def add(self, point: List[int]) -> None:
        x,y = point
        self.points[(x,y)]+=1 ## adding the point to hash map and updating the freq
        

    def count(self, point: List[int]) -> int:
        x1,y1 = point ## this is the query point
        ## we need to check this point against the existing points in vault
        ## for square formation
        result = 0
        for (x2,y2), freq in self.points.items():

            ## check if this is a not a diagonal point
            if abs(x2-x1) != abs(y2-y1):
                continue
            
            if x1 == x2:
                continue
            
            ## yes, this particular point is the diagonal
            p1 = (x1,y2)
            p2 = (x2,y1)

            result+= (freq * self.points.get(p1,0) * self.points.get(p2,0))
        
        return result
        
