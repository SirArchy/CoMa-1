"""
1. Initialize the n variable to the length of the input list arr. If the length of arr is less than or equal to 2,
    return n as the result, because any sublist with length less than or equal to 2 is considered unimodal.

2. Initialize two arrays, inc and dec, with length n and all elements set to 1. 
    These arrays will store the length of the longest increasing and decreasing sublists ending at each index of arr, respectively.

3. Use a for loop to iterate over the input list arr from index 1 to index n,
    updating the inc array. If the current element arr[i] is greater than or equal to the previous element arr[i-1], 
    we set inc[i] = inc[i-1] + 1, because this means that arr[i] can be added to the end of the longest increasing sublist ending at arr[i-1].

4. Use another for loop to iterate over the input list arr in reverse order, from index n-2 to -1, updating the dec array.
    If the current element arr[i] is greater than or equal to the next element arr[i+1], we set dec[i] = dec[i+1] + 1,
    because this means that arr[i] can be added to the end of the longest decreasing sublist starting from arr[i+1].

5. Initialize a variable max_len to store the length of the longest unimodal sublist. 
    Use another for loop to iterate over the input list arr and update max_len with the maximum of inc[i] + dec[i] - 1 for all i. 
    This represents the length of the longest unimodal sublist ending at index i 
    that consists of the longest increasing sublist ending at i and the longest decreasing sublist starting from i.

6. Return max_len as the result of the function.
"""


def maxunimod(arr):
    n = len(arr)
    if n <= 2:
        return n
    inc, dec = [1] * n, [1] * n
    for i in range(1, n):
        if arr[i] >= arr[i-1]:
            inc[i] = inc[i-1] + 1
    for i in range(n-2, -1, -1):
        if arr[i] >= arr[i+1]:
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