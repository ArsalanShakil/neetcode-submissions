class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        sol = []
        n = len(nums)
        def backtrack(i, curSum):
            if curSum == target:
                res.append(sol.copy())
                return
            if i == n or curSum > target:
                return
            sol.append(nums[i])
            backtrack(i, curSum + nums[i])
            sol.pop()
            backtrack(i+1, curSum)
            
        backtrack(0,0)
        return res