class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # I tried to dfs a Bfs problem..
        #
        
        # if location is treasure return 0

        # Questions/ edge cases:  
        # - What do we want to return? Are we modifying the original grid or make new one
        # - DFS. Seems like the base case is when we find a 0 in the grid, however... that 
        # is not always going to happen. e.g. a 1 sized grid with only -1
        # Struggling with thinking my plan out all thr way through.

        ROWS, COLS = len(grid), len(grid[0])

        def dfs(self, r, c): # do I need to pass grid as parameter here?

            if grid[r][c] == 0:
                return 0
            elif 
                r < 0 or
                c < 0 or
                r > len(grid)-1 or
                c > len(grid[0] - 1) or
                grid[r][c]== -1 : return 0
            else: # we can actually count in that direction so get the min of all 4 directions for nearest chest.
                #if im on land, i can only count in the next direction if it is lando or a treasure chest;
                #if any step around me is a treasure chest I return 1 plus the accumulation of steps it took to get there.
                grid[r][c] = min(dfs()) # keep forgetting if i need to use self to refernce this recursive function.

             


        dfs(0,0)
        return None
