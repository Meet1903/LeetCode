class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        dict1 = {}
        for index, i in enumerate(strs):
            s = ''.join(sorted(i))
            if s in dict1.keys():
                l = dict1[s]
                l.append(index)
                dict1[s] = l
            else:
                dict1[s] = [index]
        
        for key in dict1.keys():
            l = dict1[key]
            l2 = []
            for i in l:
                l2.append(strs[i])
            result.append(l2)
        
        return result