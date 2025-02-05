class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sa = list(s) # Version 1 (inefficient)
        # ta = list(t)
        # return sorted(sa) == sorted(ta)

        count = [0] * 26 # Version 2 (efficient)
        for i in s:
            count[ord(i) - ord('a')] += 1
        for i in t:
            count[ord(i) - ord('a')] -= 1
        for j in count:
            if j != 0:
                return False
        return True        
