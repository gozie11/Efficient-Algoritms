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
