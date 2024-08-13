class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        visited = {}
        start, current, local_max, global_max = 0, 0, 0, 0
        for current in range(0, len(s)):
            current_char = s[current]
            if current_char in visited:
                evaluating = visited[current_char]
                if evaluating >= start:
                    start = visited[current_char] + 1
            visited[current_char] = current
            local_max = (current - start) + 1
            if local_max > global_max:
                global_max = local_max
        return global_max
