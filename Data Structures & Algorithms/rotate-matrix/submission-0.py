class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        ## Bro lets not complete this
        ## for rotating a sqaure matric 90. You need 
        ## Transpose, Do a Horizontal reflection

        n = len(matrix) ## square right

        ## do the Transpose of a matrix

        for i in range(n):
            for j in range(i+1,n):
                matrix[i][j], matrix[j][i] = matrix[j][i],matrix[i][j]
                ## basic python variable swaping without the need for temp
        
        ## Horizontal Rotation, HR

        for i in range(n):
            for j in range(n//2):
                matrix[i][j],matrix[i][n-j-1] = matrix[i][n-j-1],matrix[i][j]

        
        