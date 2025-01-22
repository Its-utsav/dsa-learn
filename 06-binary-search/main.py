from typing import List


class Binary_Search_Solution:
    """
    effecient searching algorithm , by reducing search range
    """

    def bs_iterative(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (low + high) // 2
            # print(nums[low:high])
            if nums[mid] == target:
                return mid
            elif target > nums[mid]:
                # go right
                low = mid + 1

            # elif nums[mid] > target:
            #     high = mid - 1
            else:
                high = mid - 1

        return -1

    def bs_recursive(self, nums: List[int], target: int, low: int, high: int) -> int:
        # base case
        if low > high:
            return -1
        # recurive case
        mid = (low + high) // 2

        if nums[mid] == target:
            return mid
        elif target > nums[mid]:
            return self.bs_recursive(nums, target, mid + 1, high)
        else:
            return self.bs_recursive(nums, target, low, mid - 1)

    def lower_bound(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = n
        low = 0
        high = n - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] >= target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def upper_bound(self, nums: List[int], target: int) -> int:
        n = len(nums)
        ans = n
        low = 0
        high = n - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] > target:
                ans = mid
                high = mid - 1
            else:
                low = mid + 1

        return ans

    def search_insert(self, nums: List[int], target: int) -> int:
        """
        Return an index of target element from DS
        If element not found in DS than it return the ideal position for element in DS so that DS remain in sorted order
        """
        return self.lower_bound(nums, target)

    def find_floor_and(self, nums: List[int], target: int) -> List[int]:
        """ """
        return []

    def searching_rotated_sorted(self, nums: List[int], target: int) -> int:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (high + low) // 2
            # print(nums[low:high], nums[mid])

            if nums[mid] == target:
                return mid

            # identify sorted half
            if nums[low] <= nums[mid]:
                # left side is sorted
                if nums[low] <= target <= nums[mid]:
                    # check if target located between sorted half range
                    # close to the target
                    # if yes than high = mid -1
                    high = mid - 1
                else:
                    # no means need more higher value
                    # low should be increse
                    low = mid + 1
                # no than  low = mid + 1

            else:
                # right side is sorted
                if nums[mid] <= target <= nums[high]:
                    # check if target located between sorted half range
                    low = mid + 1
                else:
                    high = mid - 1
            # if yes than low = mid + 1
            # no than high = mid - 1
        return -1

    def searching_rotated_sorted_with_duplicates(
        self, nums: List[int], target: int
    ) -> bool:
        n = len(nums)
        low = 0
        high = n - 1

        while low <= high:
            mid = (high + low) // 2
            print(nums[low:high], nums[mid])

            if nums[mid] == target:
                return True

            if nums[low] == nums[mid] == nums[high]:
                low += 1
                high -= 1
                continue
            # identify sorted half
            if nums[low] <= nums[mid]:
                # left side is sorted
                if nums[low] <= target <= nums[mid]:
                    # check if target located between sorted half range
                    # close to the target
                    # if yes than high = mid -1
                    high = mid - 1
                else:
                    # no means need more higher value
                    # low should be increse
                    low = mid + 1
                # no than  low = mid + 1

            else:
                # right side is sorted
                if nums[mid] <= target <= nums[high]:
                    # check if target located between sorted half range
                    low = mid + 1
                else:
                    high = mid - 1
            # if yes than low = mid + 1
            # no than high = mid - 1
        return False

    def find_min(self, nums: List[int]) -> int:
        return min(nums)

    def find_peak(self, nums: List[int]) -> int:
        n = len(nums)
        for i in range(len(nums)):
            if (i == 0 or nums[i - 1] < nums[i]) and (
                i == n - 1 and nums[i] > nums[i - 1]
            ):
                return i
        return -1


def main() -> None:
    s = Binary_Search_Solution()
    arr = [3, 2, 1]  # [1,2,1,3,5,6,4]

    ans = s.find_peak(arr)
    print(ans)


if __name__ == "__main__":
    main()
