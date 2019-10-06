class Solution(object):
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        candidates.sort() # 先排序防止之后出现重复的情况
        if target == 0:
            return [[]]
        if not candidates or target < min(candidates):
            return []
        res = []
        for i in range(len(candidates)):
            target = target - candidates[i]
            for j in self.combinationSum(candidates[i:], target):
                res.append([candidates[i]] + j)
            target = target + candidates[i]
        return res


test = Solution()
print(test.combinationSum([2,3,5], 8))
