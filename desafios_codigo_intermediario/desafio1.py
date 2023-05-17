T = int(input())

for _ in range(T):
    N, K = map(int, input().split())
    total = (N // K) + (N % K)  # Calcula o número total de garrafas
    print(total)