Given an integer n, return an array ans of length n + 1 such that for each i (0 <= i <= n), ans[i] is the number of 1's in the binary representation of i.

There is very naive solution in O(n log n). Iterating the numbers and doing euclidian division and computing the rests.
There is also a solution on very efficient relies on bits. We know that :
- i >> 1 is equivalent to i // 2. It shifts the bits of i one position to the right.
- i & 1 checks if the last bit is 1 (i.e., if the number is odd).

The value at result[i] is the sum of result[i // 2] (which is the number of 1s in i // 2) and i & 1 (which adds 1 if i is odd).
i.e 
- 4 // 2 = 2    101  => 2 ones 
- 5 // 2 = 2    111  => 2  + odd bit = 3 ones.
Complexity O(n). Execution example:
```python
result[1] = result[1] + 1 => result[1] = 1
result[2] = result[1] + 0 => result[2] = 1
result[3] = result[1] + 1 => result[3] = 2
result[4]  =result[2] + 0  => result[4] = 1
result[5] = result[2] + 1 => result[5] = 2
```

