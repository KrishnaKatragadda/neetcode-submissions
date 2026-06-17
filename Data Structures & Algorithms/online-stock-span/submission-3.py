class StockSpanner:

    def __init__(self):
        self.stack = []

        ## i see that there is incoming data stream and i 
        ## need to compare the incoming with the existing people
        ## so stack
        

    def next(self, price: int) -> int:
        span = 1 ## every element is elible for 1

        while self.stack and self.stack[-1][0]<=price:
            prev_span = self.stack.pop()[1]
            span+=prev_span
        
        self.stack.append((price,span))

        return span

        


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)