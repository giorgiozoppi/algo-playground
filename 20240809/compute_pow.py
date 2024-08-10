class Solution:
    def compute_pow(self, x, n) -> float:
        pow_value = 1
        while n > 0:
            pow_value = x * pow_value 
            n = n - 1
        return pow_value

    def myPow(self, x: float, n: int) -> float:
        pow_value = 1
        if n >=0:
            if n == 0:
                return 1
            else:
                pow_value = self.compute_pow(x, n) 
        else:
            pow_value = 1 / self.compute_pow(x, -n)

        return pow_value