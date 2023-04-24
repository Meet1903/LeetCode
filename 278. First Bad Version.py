# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        # while (n >= 0):
        #     if(isBadVersion(n) and not isBadVersion(n-1)):
        #         return n
        #     n -= 1
        if n ==1 or isBadVersion(1):
            return 1
        l = 1
        r = n
        while l <= r:
            if r - l == 1:
                return r
            else:
                mid = l + (r-l)//2
                if isBadVersion(mid):
                    r = mid
                else:
                    l = mid