class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        countS = {}
        countT = {}

        if len(s) != len(t):
            return False

        for element in range(len(s)):
            countS[s[element]] = 1+countS.get(s[element],0)
            countT[t[element]] = 1+countT.get(t[element],0)

        
        return True if countS == countT else False