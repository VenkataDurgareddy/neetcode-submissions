class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashtable={}
        for i in strs:
            str1=tuple(sorted(i))
            if str1 in hashtable:
                hashtable[str1].append(i)
            else:
                hashtable[str1]=[i]
        result=[]
        for i in hashtable:
            result.append(hashtable[i])

        return result
