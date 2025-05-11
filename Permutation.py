class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = nums.length
        res = []
        sol = []

        def backTrack():
            if len(sol) == n:
                res.append(sol.copy())
                return

            for each in nums:
                if each not in sol:
                    sol.append(each)
                    backTrack()
                    sol.pop()

            backTrack()
            return res
