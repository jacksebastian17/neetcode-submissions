class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        m = len(matrix)
        n = len(matrix[0])
        print("m", m)
        print("n", n)
        newMatrix = [[0 for _ in range(m)] for _ in range(n)]
        for i in range(n): # row (0,3)
            for j in range(m): # col (0,2)
                newMatrix[i][j] = matrix[j][i]
                print("[i,j] = " + "[" + str(i) + "," + str(j) + "]")
        return newMatrix