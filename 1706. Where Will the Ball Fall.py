class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        
        ansTable = [[-2 for i in range(101)] for j in range(101)]
        m = len(grid)
        n = len(grid[0])
        def isValid(i,j):
            return i >= 0 and i < m and j >=0 and j < n
        
        def fallOrNot(i, j):
            if (i == m):
                return j
            if(isValid(i,j)):
                if (grid[i][j] == 1 and isValid(i, j+1) and grid[i][j+1] == 1):
                    if ansTable[i+1][j+1] != -2:
                        return ansTable[i+1][j+1]
                    else:
                        ansTable[i+1][j+1] = fallOrNot(i+1, j+1)
                        return ansTable[i+1][j+1]
                if (grid[i][j] == -1 and isValid(i, j-1) and grid[i][j-1] == -1):
                    if ansTable[i+1][j-1] != -2:
                        return ansTable[i+1][j-1]
                    else:
                        ansTable[i+1][j-1] = fallOrNot(i+1, j-1)
                        return ansTable[i+1][j-1]
            return -1
        # print(ansTable)
        ans = []
        for i in range(len(grid[0])):
            ans.append(fallOrNot(0, i))
        return ans
        