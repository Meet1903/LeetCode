class Solution:
    def isValid(self, s: str) -> bool:
        curly = 0
        roundBracket = 0
        squareBracket = 0
        stack = []
        dict1 = {')':'(', '}':'{', ']':'['}
        for i in s:
            if i == '(' or i=='[' or i == '{':
                stack.append(i)
            else:
                try:
                    p = stack.pop()
                    print(p)
                    if p != dict1[i]:
                        return False
                except:
                    return False
        if len(stack) > 0:
            return False
        return True