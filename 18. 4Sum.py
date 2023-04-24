class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        nums.sort()
        for i in range(len(nums) - 2):
            for j in range(i+1, len(nums) -1):
                # if nums[j] == nums[j-1]:
                #     continue
                l, r = j+1, len(nums) - 1
                while (l < r):
                    res = nums[i] + nums[j] + nums[l] + nums[r]
                    if res < target:
                        l += 1
                    elif res > target:
                        r -= 1
                    else:
                        if [nums[i]]+[nums[j]]+[nums[l]]+[nums[r]] not in result:
                            result.append([nums[i]]+[nums[j]]+[nums[l]]+[nums[r]])
                        l += 1
                        # while l < r and nums[l] == nums[l-1]:
                        #     l += 1
                # else:
                #     return result
        return result