from typing import List


class Solution:
    def digit_total(self, target: int, num: int) -> bool:
        if num < target:
            return False

        if target == num:
            return True

        return self.digit_total(target, num // 10)

    def punishmentNumber(self, num: int) -> int:
        nums = []  # numbers that square's sum equals to the number itself
        ans = 0
        for i in range(1, num + 1):
            square = i * i
            # print(i, nums, square)

            if self.digit_total(i, square):
                ans += square
                print(i)

        print(ans)

    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        score.sort()
        # n = len(score[0]) - 1
        # for i in range(len(score)):
        #     print(score[i][k])
        return score


s = Solution()
print(s.sortTheStudents([[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]], 2))
# print(s.punishmentNumber(37))
