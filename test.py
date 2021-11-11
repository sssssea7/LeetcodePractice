def q1(A):
    n = len(A)
    ans = [0] * n
    step = 1
    while step<=n:
        for j in range(0, n, step):
            ans[j] = ans[j]+A[j]
        print(ans, step)
        step *= 2
        
def q2(A):
    n = len(A)
    for i in range(n):
        j = 1
        while j<n:
            if i%j==0:
                A[i] = A[i] + A[j]
            j *= 2
            print(A)




A = [1,2,3,4,5,6,7,8]
q2(A)