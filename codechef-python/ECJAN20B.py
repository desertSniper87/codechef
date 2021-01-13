# cook your dish here

t = int(input())

for _ in range(t):
    N, M, K = map(int, input().split())

    total = N + M

    buy_round = K // total
    extra = K % total
    print(buy_round * N + ( min(extra, N) ))


