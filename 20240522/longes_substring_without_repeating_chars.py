class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        length_list = []
        visited = set()
        k = 0
        for c in s:
            if c in visited:
                visited.clear()
                length_list.append(k) 
                visited.add(c)
                k = 1
            else:
                visited.add(c)
                k = k + 1
        x = max(length_list)
        return x
