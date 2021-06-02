class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix[0])):
            for j in range(i,len(matrix[0])):
                            matrix[j][i],matrix[i][j]=matrix[i][j],matrix[j][i]
        for i in range(len(matrix[0])):
            matrix[i].reverse()
        return matrix
