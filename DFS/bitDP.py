def bit_dp(N, Adj):
    dp = [[0]*N for i in range(1 << N)]
    # dp({0}, 0) = 1 と初期化する
    dp[1][0] = 1

    # S = 頂点の集合
    for S in range(1 << N):
        # v = 最後に到達する頂点
        for v in range(N):
            # v が S に含まれていないときはパスする
            if (S & (1 << v)) == 0:
                continue

            # Sからvを除いた頂点の集合を全て通り，最後にuを通り
            # その後，uとvを繋ぐパスを通りvに到達する
            # sub = S - {v}
            sub = S ^ (1 << v)

            for u in range(N):
                # sub に u が含まれており、かつ u と v が辺で結ばれている
                if (sub & (1 << u)) and (Adj[u][v]):
                    dp[S][v] += dp[sub][u]

    ans = sum(dp[(1 << N) - 1][u] for u in range(1, N))
    return ans


def main():
    N, M = map(int, input().split())
    Adj = [[0]*N for i in range(N)]

    for _ in range(M):
        a, b = map(int, input().split())
        Adj[a-1][b-1] = 1
        Adj[b-1][a-1] = 1

    ans = bit_dp(N, Adj)

    print(ans)


if __name__ == '__main__':
    main()