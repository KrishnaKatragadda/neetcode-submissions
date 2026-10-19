class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        q = deque() ## stores the indices of the current element
        res = []

        for  r in range(len(nums)):

            ##step1 - eliminate all the kings, if they are not in window
            if q and q[0] <=r-k:
                q.popleft()
            
            ##step2 - remove any elements who are less than incoming

            while q and nums[q[-1]]<=nums[r]:
                q.pop()
            
            ##step3, add the incoming
            q.append(r)

            ##step4 - declare the king, assign the maximum 
            if r>=k-1:
                res.append(nums[q[0]])
        
        return res