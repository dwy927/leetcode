比较简单的动态规划

dp[0] = nums[0]
dp[1] = max(dp[0], nums[1])
dp[i] = max(dp[i-1], dp[i-2]+nums[i])
ans = dp[-1]

注意边界条件：输入数组为0时，输出0
