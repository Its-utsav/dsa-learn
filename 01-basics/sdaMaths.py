import math
from typing import List


class Solution:
    def countDigit(self, x: int) -> int:
        return int(math.log10(x) + 1)

    def reverse(self, x: int) -> int:
        """
        TC -> O(log n)
        SC -> O(1)
        """
        rev = 0
        if x < 0:
            temp = int(math.fabs(x))
        else:
            temp = x

        while temp != 0:
            rem = int(temp % 10)
            rev = rem + rev * 10
            temp //= 10

        if temp > ((2**31) - 1) and temp > (2**31):
            return 0
        elif x < 0:
            return -rev
        else:
            return rev

    def isPalindrome(self, x: int) -> bool:
        """
        TC -> O(log n)
        SC -> O(1)
        """
        rev = 0
        if x < 0:
            temp = int(math.fabs(x))
            return False
        else:
            temp = x

        while temp != 0:
            rem = int(temp % 10)
            rev = rem + rev * 10
            temp //= 10

        return rev == x

    def armstrongNumber(self, n) -> bool:
        """
        SC O(1)
        TC O(log n)
        """
        countNum: int = int(math.log10(n) + 1)
        if countNum > 3 and n < 0:
            return False

        arm: int = 0
        temp: int = n

        while temp != 0:
            rem = int(temp % 10)
            powTotal = rem**countNum
            arm = arm + powTotal

            temp //= 10

        return arm == n

    def sum_of_divisor(self, n: int) -> int:
        count = 0
        for i in range(1, n + 1):
            if n % i == 0:
                count += i

        return count

    def sumOfAllDivisors(self, n: int) -> int:
        total_of_divisor = 0
        for i in range(1, n + 1):
            # print(i, self.sum_of_divisor(i))
            total_of_divisor += self.opt_sum_of_divisor(i)

        return total_of_divisor

    def opt_sumOfAllDivisors(self, n: int) -> int:
        temp = []
        total = 0
        newN = int(math.sqrt(n))
        for i in range(1, newN + 1):
            if n % i == 0:
                temp.append(i)

            # counter part
            if i != n // i:
                temp.append(n // i)

        print(temp)
        for i in temp:
            total += self.sum_of_divisor(i)
        return total

    def sumOfDiv(self, n: int) -> int:
        total = 0
        temp = []
        newN = int(math.sqrt(n))
        for i in range(1, newN + 1):
            if n % i == 0:
                temp.append(i)

            if n // i != i:
                temp.append(n // i)

        print(temp)
        for i in temp:
            total += i
        return total

    def sumOfDivisors_opt(self, n: int) -> int:
        if n <= 0:
            return 0
        ans = 0
        for i in range(1, n + 1):
            div = n // i
            ans += div * i
        return ans

    def gcd_lcm1(self, n1: int, n2: int) -> List[int]:
        gcd = 1
        for i in range(1, (min(n1, n2) + 1)):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i

        lcm = int((n1 * n2) / gcd)

        return [lcm, gcd]

    def gcd_lcm2(self, n1: int, n2: int) -> List[int]:
        gcd = 1

        for i in range(min(n1, n2), 1, -1):
            if n1 % i == 0 and n2 % i == 0:
                gcd = i
                break

        lcm = int((n1 * n2) / gcd)
        return [lcm, gcd]

    def eulidan_algo(self, n1: int, n2: int) -> int:
        """
        TC-> O(min(n1,n2))
        """
        gcd = 1
        if n1 < 0 and n2 < 0:
            return 1
        if n2 > n1:
            [n1, n2] = [n2, n1]

        while n2 != 0:
            rem = int(n1 % n2)
            n1 = n2
            n2 = rem

        gcd = n1
        return gcd

    def gcd_lcm3(self, n1: int, n2: int) -> List[int]:
        """
        TC -> O(min(n1,n2))
        SC -> O(1)
        """
        gcd = self.eulidan_algo(n1, n2)

        lcm = int((n1 * n2) / gcd)
        return [lcm, gcd]

    def is_prime(self, number: int) -> bool:
        if number < 1:
            return False
        count = 0
        for i in range(1, int(math.sqrt(number)) + 1):
            if number % i == 0:
                count += 1

                if number // i != i:
                    count += 1

        if count == 2:
            return True
        else:
            return False


sol = Solution()
print(sol.is_prime(7))
# print(sol.sumOfDivisors_opt(1))
# print(sol.opt_sumOfAllDivisors(5))
# print(sol.opt_sumOfAllDivisors(1))
