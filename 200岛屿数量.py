# 递归的方向很重要 上、下、左、右
# 和前面的括号生成一样，要有一种方位感
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m=len(grid)
        n=len(grid[0])
        count=0

        def dfs(i,j):
            if i>=m or i<0 or j>=n or j<0 or grid[i][j]=='0':
                return 

            grid[i][j] = '0'

            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i,j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]=='1':
                    count+=1
                    dfs(i,j)

        return count
