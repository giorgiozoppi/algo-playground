from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result list with zeros
        result = [0] * (n + 1)        
        # Fill the result list using the relationship
        for i in range(1, n + 1):
            result[i] = result[i >> 1] + (i & 1)
            print(result[i])
        return result

if __name__ == "__main__":
    s = Solution()
    s.countBits(5)