class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0                            # 1. Initialize result container to 0
        for i in range(32):                # 2. Loop 32 times (for each bit position 0 to 31)
            bit = (n >> i) & 1             # 3. Isolate the i-th bit from the right of n
            res = res | (bit << (31 - i))  # 4. Place that bit into its mirrored position in res
        return res                         # 5. Return the fully reversed integer

