class Solution:

    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)
        count = {n: 0 for n in nums}
        for e in nums:
            count[e] += 1

        def backTrack():
            if len(sol) == n:
                res.append(sol.copy())
                return

            for i in count:
                if count[i] > 0:
                    sol.append(i)
                    count[i] -= 1
                    backTrack()
                    sol.pop()
                    count[i] += 1
        backTrack()
        return res
