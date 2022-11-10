def quicksort(list, pivotFunction):
    return None


def partition(list, lo, hi, pivotFunction):
    pivot = pivotFunction(list, lo, hi)
    list[lo:hi + 1]
    return None


def pivotFunction(list, lo, hi):
    return None


L = [18, 32, 9, 27, 28, 21, 29, 7, 12, 4]
quicksort(L, pivotFunction)
print(L)

L = [4, 5, 3, 2, 12, 13, -8, -19, -4, 9, 19, 11, -2]
partition(L, 3, 8, pivotFunction)
print(L)
