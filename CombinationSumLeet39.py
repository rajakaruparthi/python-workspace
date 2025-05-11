class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []

        def backtrack(i, nums, cal):
            if cal == target:
                res.append(nums.copy())
                return

            if cal > target or i >= len(candidates):
                return

            nums.append(candidates[i])
            backtrack(i, nums, cal + candidates[i])
            nums.pop()
            backtrack(i + 1, nums, cal)

        backtrack(0, [], 0)
        return res
