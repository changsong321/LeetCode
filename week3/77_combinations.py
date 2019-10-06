class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """
        arr = [i for i in range(1, n + 1)]
        ans = []
        a = []

        def dfs(array, k):
            if k == 0:
                ans.append(a.copy())
                return
            for i in range(len(array)):
                a.append(i)
                dfs(arr[i + 1:], k - 1)
                a.pop()
        dfs(arr, k)
        return ans

test = Solution()
print(test.combine(4,2))

