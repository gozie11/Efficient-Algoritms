#07/27/24 2:21. I will track elapsed time to write the solution and do all checks next time.
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # U: want to return the minimum amount of time in takes for there to be zero fresh furits left
        # M: Going to use a BFS algorithm
        # P: visited set, q = deque, variable for elapsed time, 
        #   add all rotten fruit to q first, 
        #   mark infected fruits as such, increment time after each infection round.
        #   At the end, check each row and see if there are any fresh fruit left
        #   return time - 1 if there are no 1s, otherwise return -1 
        #I: Done
        #R: 
        #E : Down below

        #R: reflect. There's a glaring whole in my first attempt at this problem where i don't check the number of 
        #   fresh oranges I have to begin with. I will do this in the preprocessing step. This way,
        # if there are 0 fresh oranges I can automatically return 0 without doing extra work. 

        visited = set() # set of tuples
        q = deque() # list of lists
        fresh_fruit = 0

        ROWS , COLS = len(grid), len(grid[0])
        

        # add all the rotten fruit to the array firstly
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2: 
                    visited.add((r,c))
                    q.append([r,c])
                if grid[r][c] == 1: fresh_fruit += 1

        if not fresh_fruit : return 0

        def infect(r,c) -> None:
            if min(r,c) < 0 or c >= COLS or r >= ROWS or (r,c) in visited or grid[r][c] == 0: return
            grid[r][c] = 2
            #I still feel like i can get away with not using a visited set and just use the fact that the grid is 2
            visited.add((r,c))
            q.append([r,c])

        time = 0

        while q:

            for fruit in range(len(q)): # I learned that you cannot just iterate on (for fr in q) because the q changes 
                                        # during the iteration. However I guess the length doesn't change after initial 
                                        # creation of the iterator.
                #get the next fruit to be rotted
                r,c = q.popleft()

                infect(r+1, c)
                infect(r-1, c)
                infect(r, c-1)
                infect(r, c+1)

            time += 1

        for row in grid:
            # check if any fruit survived being rotted
            if 1 in row : return -1

        # Time: O(ROWS * COLS)
        # Space: O(ROWS * COLS)

        return (time - 1)









#chat GPT tweaked corrections, 

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        ROW, COL = len(grid), len(grid[0])

        if ROW == 0 or COL == 0:
            return -1

        q = deque()
        visited = set()
        fresh_oranges = 0

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2: 
                    q.append((row, col))
                    visited.add((row, col))
                elif grid[row][col] == 1:
                    fresh_oranges += 1

        if fresh_oranges == 0:
            return 0

        time = 0

        def infect(r, c):
            if (r < 0 or c < 0 or r >= ROW or c >= COL or
                (r, c) in visited or grid[r][c] != 1):
                return
            q.append((r, c))
            visited.add((r, c))
            grid[r][c] = 2

        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                infect(r + 1, c)
                infect(r - 1, c)
                infect(r, c + 1)
                infect(r, c - 1)

            time += 1

        for row in grid:
            if 1 in row:
                return -1

        return time - 1


#My initial attempt before gpt 
class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        BFS starting with the rotten bananas
        At the end check if there are any 1s left in the input
        return -1 or the current time when all the bananas have rotted
        """

        ROW, COL = len(grid) , len(grid[0])

        if not COL:
            return -1

        q = deque()
        visited = set()

        for row in range(ROW):
            for col in range(COL):
                if grid[row][col] == 2: 
                    q.append([row,col])
                    visited.add((row,col))

        def infect(r,c):
            #only add fresh bananas . I feel like if i only aded fresh , i don't have to check visited
            if (r < 0
            or c < 0
            or r >= ROW
            or c >= COL
            or grid[r][c] == 2
            or grid[r][c] == 0):
                return
            q.append([r,c])
            visited.add((r,c))

        time = 0

        # check if there are elements in the queue before incrementing the time

        while q:
            for el in range(len(q)):
                r,c = q.popleft()

                infect(r+1, c)
                infect(r-1, c)
                infect(r, c-1)
                infect(r, c+1)

            #check if everyone is infected. return time if yes
            if not any(1 in sublist for sublist in grid): 
                print("gotcha", grid)
                return time # double check
            else: time += 1

        return -1    
