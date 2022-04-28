class Solution:
    def getSum(self, a: int, b: int) -> int:
        # non-accepted method
        # return a + b

        # bit manipulation
        # --> XOR, carry, sign(both positive or negative), borrow(one pos one neg)
        # XOR get sum without carry
        # loop untile carry is 0
        # ~a ==  -a - 1
        #         13 -2
        #         13 -- 0 1 1 0 1
        #         2  -- 0 0 0 1 0
        #         ~13 - 0 1 1 1 0   <-- 14

        #               0 1 1 1 1 -- 15
        #               0 0 1 0 0 -- 4
        #               1 0 0 0 0 -- 16

        #               0 1 0 1 1 == 11
        #               0 0 0 0 0
        if abs(a) < abs(b): a, b = b, a
        sign = 1
        if a < 0: sign = -1
        mark = 1
        if a * b < 0: mark = -1
        a, b = abs(a), abs(b)
        if mark == 1:
            while b:
                a, b = a ^ b, (a & b) << 1
                # b = (a & b) << 1
        else:
            while b:
                a, b = a ^ b, (~a & b) << 1
                # b = (~a & b) << 1
        return a if sign == 1 else -a









