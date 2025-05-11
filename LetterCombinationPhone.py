class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        res = []
        number_to_char_map = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl", "6": "mno", "7": "pqrs", "8": "tuv",
                              "9": "wxyz"}

        def backtrack(i, sol):
            if len(sol) == len(digits):
                res.append(sol)
                return

            for c in number_to_char_map[digits[i]]:
                backtrack(i + 1, sol + c)

        if digits:
            backtrack(0, "")
        return res
