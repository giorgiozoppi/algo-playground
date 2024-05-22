"""

s = otato
i = 0
j = len(s)-1
j > i

i = 0, s[0] => o
j = 4, s[4] => o

i = 1, s[i] => t
j = 3, s[j] => t

i = 2, s[i] => a
j = 2  s[j] => a
True.

s = otto
i = 0, s[0] = o
j = 3, s[3] = o
i = 1, s[0] = t
j = 2, s[2] = t
j = 3, i = 3  
"""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        upper_case = s.upper()
        data = []
        alpha = list(filter(lambda s: (ord(s) >= 65 and ord(s) <= 90) or (ord(s) >=48 and ord(s) <= 57), upper_case))
        i,j = 0, len(alpha) -1
        while i<=j:
            if alpha[i]!= alpha[j]:
                return False
            else:
                i,j = i + 1, j - 1
        return True    

