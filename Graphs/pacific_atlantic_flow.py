# This one was interesting and I'm glad I deduced that I should use a dfs algorithm to solve if from the jump.
# I didn't stick through to come up with my own solution. That is ok. After a certain amount of time you should look at the solution to see if you're on the right track!

class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        ROWS, COLS = len(heights) , len(heights[0])

        pac , atl = set(), set()

        def dfs(r,c,visit, prev_height):
            if(
                (r,c) in visit 
                or r < 0 
                or c < 0 
                or r == ROWS 
                or c == COLS 
                or heights[r][c] < prev_height # critical 
            ): return
            visit.add((r,c))
            dfs(r+1, c, visit, heights[r][c])
            dfs(r-1, c, visit, heights[r][c])
            dfs(r, c-1, visit, heights[r][c])
            dfs(r, c+1, visit, heights[r][c])

        for c in range(COLS):
            dfs(0, c, pac,heights[0][c])
            dfs(ROWS - 1, c, atl ,heights[ROWS-1][c])

        for r in range(ROWS):
            dfs(r, 0, pac,heights[r][0])
            dfs(r, COLS-1, atl,heights[r][COLS-1])


        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r,c) in atl and (r,c) in pac:
                    res.append([r,c])
        
        return res
