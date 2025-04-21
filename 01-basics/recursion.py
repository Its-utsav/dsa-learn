class Solution:
    def printName(self, n: int) -> str:
        if n == 1:
            return
        else:
            print("utsav ", end="")
            self.printName(n - 1)

    def printUpToN(self, n: int) -> None:
        if n != 0:
            self.printUpToN(n - 1)
            print(n, end=" ")

    def n_to_1(self, n: int) -> None:
        if n > 0:
            print(n, end=" ")
            self.n_to_1(n - 1)

    def sumOf_3_Series(self, n):
        res = n**3
        if n == 1:
            return 1
        else:
            return res + self.sumOf_3_Series(n - 1)

    def factorialNumbers(self, n: int) -> int:
        if n == 1:
            return 1
        else:
            return n * self.factorialNumbers(n - 1)

    def fib(self, n: int) -> int:
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            return self.fib(n - 1) + self.fib(n - 2)


sol = Solution()
print(sol.fib(4))
