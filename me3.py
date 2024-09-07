def rec(n):
    if n<=0:
        return n
    return n+rec(n-1)
n=10
print(rec(n))

    