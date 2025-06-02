class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        
        def find_it( target : int) -> int:
            left , right = 0, len(nums2)-1

            while left <= right : 
                mid = (left + right) // 2

                if nums2[mid] == target:
                    return mid
                elif nums2[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1 
            return -1

        for num in nums1:
            if find_it(num) != -1:
                return num
        return -1
