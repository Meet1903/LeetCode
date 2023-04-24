class Solution:
    def shortestPath(self, grid: List[List[int]], k: int) -> int:
        visited = [[ [False for col in range(k+1)] for col in range(len(grid[0]))] for row in range(len(grid))]
        print(visited)
        direction = [[0,1], [1,0], [0,-1], [-1,0]]
        steps = 0
        queue = [[0,0,k]]
        m = len(grid)
        n = len(grid[0])
        while (len(queue) > 0):
            size = len(queue)
            while (size > 0):
                q = queue.pop(0)
                if (q[0] == m-1 and q[1] == n-1):
                    return steps
                for d in direction:
                    i = q[0] + d[0]
                    j = q[1] + d[1]
                    obstacle = q[2]
                    
                    if ( i >= 0 and i < m and j >=0 and j < n):
                        if (grid[i][j] ==0 and not visited[i][j][obstacle]):
                            visited[i][j][obstacle] = True
                            queue.append([i,j,obstacle])
                        elif (grid[i][j] ==1 and obstacle > 0 and not visited[i][j][obstacle-1]):
                            visited[i][j][obstacle - 1] = True
                            queue.append([i,j, obstacle-1])
                size -= 1
            steps += 1
        return -1