class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
# Version 1 (inefficient)
        # sa = list(s) 
        # ta = list(t)
        # return sorted(sa) == sorted(ta)
# Version 2 (efficient)
        count = [0] * 26 
        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in t:
            count[ord(i) - ord('a')] -= 1
        for j in count:
            if j != 0:
                return False
        return True        
