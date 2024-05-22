class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        frequency_s = {}
        frequency_t = {}
        if len(s) != len(t):
            return False
            
        for c in s: 
            if c in frequency_s:
                frequency_s[c] = frequency_s[c] + 1
            else:
                frequency_s[c] = 1
        for k in t:
            if k in frequency_t:
                frequency_t[k] = frequency_t[k] + 1
            else: 
                frequency_t[k] = 1
        for key, value in frequency_s.items():
            if frequency_t.get(key) != value:
                return False
        return True
        
