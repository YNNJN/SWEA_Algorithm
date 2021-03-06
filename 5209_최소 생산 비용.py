def dfs(idx, result):
    global ans
    if idx == n:
        ans = min(ans, result)
        return

    if ans < result:
        return

    for i in range(n):
        if not visited[i]:
            visited[i] = 1
            dfs(idx + 1, result + arr[idx][i])
            visited[i] = 0

for tc in range(int(input())):
    n = int(input())
    arr = [list(map(int, input().split())) for _ in range(n)]
    visited = [0] * n
    ans = 10000
    dfs(0, 0)
    print('#{} {}'.format(tc+1, ans))