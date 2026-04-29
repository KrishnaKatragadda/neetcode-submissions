class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])

        top = 0
        bot = rows-1

        ## identifying the row in which the target is present

        while top <=bot:
            mid = (top+bot)//2
            if target < matrix[mid][0]:
                bot = mid-1
            elif target > matrix[mid][-1]:
                top = mid+1
            else:
                break
        
        if not (top<=bot):
            return False
        ## We have identified the row, now we need to check if the
        ## value is present in the row actually
        row = (top+bot)//2
        left = 0
        right = cols -1

        while left <= right:
            mid = (left+right)//2
            if target == matrix[row][mid]:
                return True
            elif target < matrix[row][mid]:
                right = mid -1
            else:
                left = mid + 1
        
        return False
