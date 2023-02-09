"""

"""

def maxunimod(arr):
    n = len(arr)
    inc = [1] * n
    dec = [1] * n
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                inc[i] = max(inc[i], inc[j] + 1)
            elif arr[i] < arr[j]:
                dec[i] = max(dec[i], dec[j] + 1)
    max_len = 0
    for i in range(n):
        max_len = max(max_len, inc[i] + dec[i] - 1)
    return max_len


print(maxunimod([4,5,3,2,1,3,6,4,7]))
# should return 5
print(maxunimod([10,9,8,10,6,5,4,3,2,3]))
# should return 7
print(maxunimod([10,9,8,7,6,5,4,3,2,3]))
# should return 9
print(maxunimod([10,9,8,7,6,5,4,3,2,1]))
# should return 10