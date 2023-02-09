def maxunimod(arr):
    """
    This function returns the length of the longest unimodal sublist ending 
    input: [list] | a list arr 
    output: [int] | the length of the longest unimodal sublist of arr
    """
    n = len(arr)
    if n <= 2:
        return n
    inc, dec = [1] * n, [1] * n
    for i in range(1, n): #increasing sublists
        if arr[i-1] <= arr[i]  :
            inc[i] = inc[i-1] + 1
    for i in range(n-2, -1, -1): #decreasing sublists
        if arr[i+1] <= arr[i]  :
            dec[i] = dec[i+1] + 1
    max_len = 0
    for i in range(n):
        max_len = max(max_len, inc[i] + dec[i] - 1)
    return max_len
    

"""
print(maxunimod([4, 2, 2, 2, 1]))
# should return 5
print(maxunimod([3, 3, 3, 4, 2]))
# should return 5
print(maxunimod([0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
# should return 10
print(maxunimod([4,5,3,2,1,3,6,4,7]))
# should return 5
print(maxunimod([10,9,8,10,6,5,4,3,2,3]))
# should return 7
print(maxunimod([10,9,8,7,6,5,4,3,2,3]))
# should return 9
print(maxunimod([10,9,8,7,6,5,4,3,2,1]))
# should return 10
"""
