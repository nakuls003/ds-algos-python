def insertion_sort(A):
    """Sorts a list A in non-decreasing order"""
    for i in range(1, len(A)):
        curr = A[i]
        j = i
        while j > 0 and A[j-1] > curr:
            A[j] = A[j-1]
            j -= 1
        A[j] = curr


if __name__ == '__main__':
    print("Enter a sequence of numbers to sort:")
    arr = [int(num)for num in input().split()]
    print("After sorting:")
    insertion_sort(arr)
    print(' '.join(str(num) for num in arr))
