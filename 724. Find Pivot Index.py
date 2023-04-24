class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        weightOnLeft = 0
        weightOnRight = sum(nums)
        
        for index,i in enumerate(nums):
            weightOnRight -= i
            if weightOnLeft == weightOnRight:
                return index
            weightOnLeft += i
        return -1