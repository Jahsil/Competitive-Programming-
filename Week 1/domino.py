def domino(M, N):
    return (M * N) // 2

def test_domino():
    arr = input().split()
    M = int(arr[0])
    N = int(arr[1])
    print(domino(M, N))
test_domino()
