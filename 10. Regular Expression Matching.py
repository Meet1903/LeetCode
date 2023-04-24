class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        cacheDict = {}
        def regMatch(i, j):
            if (i,j) in cacheDict:
                return cacheDict[(i,j)]
            if i >= len(s) and j >= len(p):
                return True
            if j >= len(p):
                return False
            
            match = i < len(s) and (s[i] == p[j] or p[j] == '.')
            if (j+1) < len(p) and p[j+1] == '*':
                cacheDict[(i,j)] = regMatch(i, j+2) or (match and regMatch(i+1,j))
                return cacheDict[(i,j)]
            if match:
                cacheDict[(i,j)] = regMatch(i+1, j+1)
                return cacheDict[(i,j)]
            cacheDict[(i, j)] = False
            return False
        
        return regMatch(0,0)