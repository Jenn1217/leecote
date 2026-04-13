class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])

        def dfs(i,j,k):
            if k==len(word):
                return True
            
            if i>=m or j>=n or board[i][j]!=word[k] or i<0 or j<0:
                return False

            tmp=board[i][j]
            board[i][j] = "#"

            res=(dfs(i+1,j,k+1) or 
            dfs(i-1,j,k+1) or 
            dfs(i,j+1,k+1) or 
            dfs(i,j-1,k+1))

            board[i][j]=tmp

            return res

        for i in range(m):
            for j in range(n):
                if dfs(i,j,0):
                    return True

        return False




            
