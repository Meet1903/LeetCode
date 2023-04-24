class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        
        result = []
        digitToCharacters = {'2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl', '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        def backtracking(i, currentString):
            if len(currentString) == len(digits):
                result.append(currentString)
                return
            for s in digitToCharacters[digits[i]]:
                backtracking(i+1, currentString + s)
                
        if digits:
            backtracking(0, '')
        return result
        