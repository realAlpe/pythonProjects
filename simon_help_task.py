def galton(m, n):
    if m < n:
        return 0
    else:
        if n == 0:
            return 1
        else:
            return galton(m - 1, n - 1) + galton(m - 1, n)


def galton2(m, n):
    if m < n:
        return 0

    # Create a two-dimensional list to store the computed values
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    # Initialize the base cases
    for i in range(m + 1):
        dp[i][0] = 1

    # Fill in the table using dynamic programming
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            dp[i][j] = dp[i - 1][j - 1] + dp[i - 1][j]

    return dp[m][n]
