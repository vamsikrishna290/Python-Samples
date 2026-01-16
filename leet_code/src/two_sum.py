from typing import List


class Solution:
    @staticmethod
    def two_sum(nums: List[int], target: int) -> List[int]:
        arr = []
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    arr.append([i,j])

        return arr

    @staticmethod
    def two_sum_with_dict(nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i
        return []


if __name__ == '__main__':
    sol = Solution()
    print(sol.two_sum([2,7,11,15, 6, 3], 9))
    print(sol.two_sum_with_dict([2,7,11,15, 6, 3], 9))