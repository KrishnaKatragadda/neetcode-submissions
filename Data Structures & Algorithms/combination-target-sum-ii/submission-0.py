class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res =[]

        candidates.sort()

        def dfs(i, curr, total):
            if total == target:
                res.append(curr.copy())
                return
            
            if total>target or i >= len(candidates):
                return
            
            ## considering the current element
            curr.append(candidates[i])
            dfs(i+1, curr, total+candidates[i])

            ## not considering the current element
            curr.pop()

            while i+1 <len(candidates) and candidates[i]==candidates[i+1]:
                ## checking if the next element is duplicate
                i+=1 ## id Yes,skip the next element and move on

            dfs(i+1, curr,total)

        dfs(0,[],0)

        return res
        
