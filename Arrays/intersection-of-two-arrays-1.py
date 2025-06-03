class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        found = {} # Hint: this can easily just be a set()

        for num in nums1:
            if num not in found:
                found[num] = 0
            
        for num in nums2:
            if num in found:
                found[num] += 1
        res = []
        for num, count in found.items():
            if count > 0:
                res.append(num)

        return res
