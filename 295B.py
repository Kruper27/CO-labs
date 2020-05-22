n = int(input())
matrix = []

ans = [0] * n

for i in range(n):
    matrix.append(list(map(int, input().split())))

keys = list(map(int, input().split()))

for k in range(n - 1, -1, -1):
    for p in range(n):
        for q in range(n):
            matrix[p][q] = min(matrix[p][q], matrix[p][keys[k] - 1] + matrix[keys[k] - 1][q])

    for p in range(k, n):
        for q in range(k, n):
            ans[k] += matrix[keys[p] - 1][keys[q] - 1]

print(' '.join([str(i) for i in ans]))
