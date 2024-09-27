def decode_message(s: str, p: str) -> bool:
    m = len(s)
    n = len(p)

    # Create a DP table
    dp = [[False] * (n + 1) for _ in range(m + 1)]
    dp[0][0] = True  # Both empty string and pattern match

    # Handle patterns that start with '*'
    for j in range(1, n + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]  # '*' can match empty sequence

    # Fill in the DP table
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if p[j - 1] == '*':
                # '*' can match any sequence (including empty)
                dp[i][j] = dp[i][j - 1] or dp[i - 1][j]
            elif p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                # Match single character or '?'
                dp[i][j] = dp[i - 1][j - 1]

    return dp[m][n]

# Example Tests
print(decode_message("aa", "a"))      # Output: False
print(decode_message("aa", "*"))      # Output: True
print(decode_message("cb", "?a"))     # Output: False
print(decode_message("adceb", "*a*b")) # Output: True
print(decode_message("acdcb", "a*c?b")) # Output: False
