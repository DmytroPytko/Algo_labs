def findThreeNumbers(A, arr_size, sum):

    A.sort()
    for i in range(0, arr_size - 2):
        l = i + 1
        r = arr_size - 1
        while (l <= r):
            if (A[i] + A[l] + A[r] == sum):
                print("YES(", A[i],
                      ', ', A[l], ', ', A[r], ")");
                return True
            elif (A[i] + A[l] + A[r] < sum):
                l += 1
            else:
                r -= 1
    return False


A = [1, 2, 3, 4, 5, 6, 12, 45]
sum = 10
arr_size = len(A)

findThreeNumbers(A, arr_size, sum)
