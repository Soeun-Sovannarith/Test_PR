def lcs(X, Y):
    m, n = len(X), len(Y)
    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1, m+1):
        for j in range(1, n+1):
            if X[i-1] == Y[j-1]:
                dp[i][j] = 1 + dp[i-1][j-1]
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp[m][n]

# Example
X = "ABCBDAB"
Y = "BDCABA"
print(lcs(X, Y))  # Output: 4

print("hello world")

print("This is Longest Common Subsequences (LCS) Algorithm")


lst = ["Git", "GitHub", "GitLab", "GitAction"]

for l in lst:
  print(l)

