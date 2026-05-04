class TimeMap:

    def __init__(self):
        self.timeMap = defaultdict(list)
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.timeMap[key].append((value,timestamp))
        return
        

    def get(self, key: str, timestamp: int) -> str:

        if key not in self.timeMap:
            return ""
        l = 0
        r = len(self.timeMap[key])-1

        while l <=r:
            m  = (l+r)//2
            if timestamp == self.timeMap[key][m][1]:
                return self.timeMap[key][m][0]
            elif timestamp < self.timeMap[key][m][1]:
                r = m-1
            else:
                l = m+1
        
        if r >=0:
            return self.timeMap[key][r][0]
        return ""
        
        
        
