#2nd attempt. Working solution.
from collections import deque
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        ROWS , COLS = len(grid), len(grid[0])

        q = deque() # track where to visit next

        visited = set()

        def visit_next(r,c) -> None:
            if (
                r >= ROWS
                or r < 0
                or c >= COLS
                or c < 0
                or (r,c) in visited
                or grid[r][c] == -1 # we can't traverse water buddy
                
            ):
                return
            q.append([r,c])
            visited.add((r,c))
            
        # add all of the treasure to the q and mark them as visited
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r,c))
                    q.append([r,c]) #I'm not sure why we add tuples to the set but lists to the deque. Maybe it's so that r,c = q.popleft() works properly

        dist = 0 # we're starting from the treasure chests. Thus the starting distance to them is 0

        while q:
            for i in range(len(q)): # I'm assuming that this range does not change once initialized. This allows me to add elements to the deque without messing up the logic
                r,c = q.popleft() # get the next location to visit
                grid[r][c] = dist
                visit_next(r+1,c)
                visit_next(r-1,c)
                visit_next(r, c-1)
                visit_next(r, c+1)
            dist += 1











# 1st attempt
class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        # I tried to dfs a Bfs problem..
        #It can probably be done this way but the time complexity would be god awful.
        
        # if location is treasure return 0

        # Questions/ edge cases:  
        # - What do we want to return? Are we modifying the original grid or make new one
        # - DFS. Seems like the base case is when we find a 0 in the grid, however... that 
        # is not always going to happen. e.g. a 1 sized grid with only -1
        # Struggling with thinking my plan out all the way through.

        # I need to start trying to reverse engineer the solution when I get stuck.
        # Start with the solution in mind and then reverse the steps to get there. Talk outloud always.

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
