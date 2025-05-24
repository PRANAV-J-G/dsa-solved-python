from collections import deque
class Solution(object):
    class Pair:
        def __init__(self, row,col):
            self.row = row
            self.col =col
    def numEnclaves(self, grid):
        q=deque()
        m,n=len(grid),len(grid[0])
        vis=[[0 for _ in range(n)] for _ in range(m)]
        #first and last row
        for i in range(n):
            if(grid[0][i]==1):
                q.append(self.Pair(0,i))
                vis[0][i]=1
            if(grid[m-1][i]==1):
                q.append(self.Pair(m-1,i))
                vis[m-1][i]=1
        #first and last column
        for i in range(m):
            if(grid[i][0]==1):
                q.append(self.Pair(i,0))
                vis[i][0]=1
            if(grid[i][n-1]==1):
                q.append(self.Pair(i,n-1))
                vis[i][n-1]=1
        drow=[-1,0,1,0]
        dcol=[0,-1,0,1]
        while q:
            node = q.popleft()
            r,c=node.row,node.col
            for i in range(4):
                nrow=r+drow[i]
                ncol=c+dcol[i]
                if(0<=nrow<m and 0<=ncol<n and grid[nrow][ncol]==1 and vis[nrow][ncol]==0):
                    vis[nrow][ncol]=1
                    q.append(self.Pair(nrow,ncol))
            #uptil here we have done multisource BFS
        count=0
        for i in range(m):
            for j in range(n):
                if(grid[i][j]==1 and vis[i][j]==0):
                    count+=1
        return count
        
s = Solution()

grid  = [[1,1,0],[0,0,1],[0,1,0]]
s.numEnclaves(grid)
        
        
        
        
        
        
        
        
        
        
        
        