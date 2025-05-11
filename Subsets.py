class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []

        def backtrack(i):
            if i >= len(nums):
                res.append(sol.copy())
                return

            sol.append(nums[i])
            backtrack(i + 1)

            sol.pop()
            backtrack(i + 1)

        backtrack(0)
        return res

    subsets([1, 2, 3])
