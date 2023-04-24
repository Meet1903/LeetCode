class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(' ')
        s = s.split(' ')[0]
        for i in range(1, len(s)):
            if ord(s[i]) < 48 or ord(s[i]) > 57:
                s = s[:i]
                break
        try:
            if(int(float(s)) < -2**31):
                return -2**31
            elif (int(float(s)) > 2**31 - 1):
                return 2**31 - 1
            else:
                return int(float(s))
        except:
            return 0