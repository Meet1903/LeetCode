class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        print(nums)
        result = nums[0] + nums[1] + nums[2]
        for i in range(len(nums) - 2):
            l, r = i+1, len(nums) - 1
            while (l < r):
                res = nums[i] + nums[l] + nums[r]
                if res == target:
                    return res
                if abs(res - target) < abs(result - target):
                    result = res
                if res > target:
                    r -= 1
                elif res < target:
                    l += 1
        return result
            