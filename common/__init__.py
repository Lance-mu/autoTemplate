# _*_ coding:utf-8 _*-
# @Time：2022/7/9 17:05
# 作者：qianwulin

class Solution(object):
    def climbStairs(self, n: int) -> int:
        def dfs(i: int, memo) -> int:
            if i == 0 or i == 1:
                return 1
            if memo[i] == -1:
                memo[i] = dfs(i - 1, memo) + dfs(i - 2, memo)
            return memo[i]

        # memo: [-1] * (n - 1)
        # -1 表示没有计算过，最大索引为 n，因此数组大小需要 n + 1
        return dfs(n, [-1] * (n + 1))


if __name__ == '__main__':
    si = Solution()
    print(si.climbStairs(8))
