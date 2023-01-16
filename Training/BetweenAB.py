A, B, x = map(int, input().split())

def f(x, n):
    return x // n


if A == 0:
    print(f(B, x) + 1)
else:
    print(f(B, x) - f(A-1, x))