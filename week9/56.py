class Solution:
    def merge(self, intervals) :
        intervals.sort(key = lambda x:x[0]) # 左端点排序
        ans = []
        for item in intervals:
            if not ans or ans[-1][1] < item[0]: # 答案里最后一个区间的右端点小于当前区间的左端点，则它们没有重合，加到答案里
                ans.append(item)
            else:
                ans[-1][1] = max(ans[-1][1],item[1])
        return ans

test = Solution()
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(test.merge(intervals))