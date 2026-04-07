# BFS中使用了队列，队列是fifo，
# 可以大致这样理解：队列中总是保存最外层的陆地
# 当遇到一块新鲜陆地时，count+1
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        m=len(grid)
        n=len(grid[0])
        count=0

        ##BFS 写法
        for i in range(m):
            for j in range(n):
              # 只有新陆地才有进行下一步探索的可能
                if grid[i][j]=='1'
                    quene=deque()
                    grid[i][j]='0'

                    quene.append((i,j))

                    while(quene):
                        x,y=quene.popleft()# 接收当前坐标，从当前坐标散开

                        for dx,dy in [(1,0),(-1,0),(0,1),(0,-1)]:
                            nx, ny = dx+1,dy+1
                            if grid[nx][ny]=='1'and 0<=nx<m and  0<=ny<n:
                                count+=1
                                quene.append((nx, ny ))
                                grid[nx][ny]='0'

        return count




