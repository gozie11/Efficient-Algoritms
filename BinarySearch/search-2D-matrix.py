class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        COLS, ROWS = len(matrix[0]), len(matrix)

        # mid = ROWS // 2 # you don't want to just use Rows to calculate the mid
                        # you want to have pointers to the begining and end thatt
                        # you can use in updating the search window

        top, bot = 0 , ROWS-1


        while top <= bot:
            mid = (top + bot) // 2

            # I don't think we can short circuit any of these statements yet

            if target > matrix[mid][-1]: # the target is greater than all values in this row
                top = mid + 1
            elif target < matrix[mid][0]: #smaller than all values in row
                bot = mid -1
            else: #the target might be in this row!
                break
        

        # check if you actually found the appropriate row IMPORTANT !
        # meaning : make sure you didn't break out of while loop from out of bounds!
      
        if top > bot:
            return False # THIS LOWERCASE FALSE STOPPED ME FROM GETTING THIS RIGHT THE FIRST TIME!!!!


        #search the appropriate row!

        l, r = 0 , COLS - 1 
        

        while l <= r:
            m = (l + r) // 2

            #short circuit magic

            if matrix[mid][m] == target:
                return True
            elif matrix[mid][m] < target: # look to the right
                l = m + 1
            else:
                r = m - 1
            
        return False
            
