def upheap(A, i):
    parent = (i-1)//2
    if i > 0 and A[i] > A[parent]:
        A[i], A[parent] = A[parent], A[i]
        upheap(A, parent)

def downheap(A, i, j):
    if 2*i+1 <= j:
        large = 2*i+1
        if 2*i+2 <= j:
            if A[2*i+2] > A[2*i+1]:
                large = 2*i+2
        if A[large] > A[i]:
            A[i], A[large] = A[large], A[i]
            downheap(A, large, j)

def heap_sort(A):
    """
    Sorts an array A using the in-place heapsort algorithm
    """
    for i in range(len(A)):
        upheap(A, i)
    for j in range(len(A)-1, 0, -1):
        A[0], A[j] = A[j], A[0]
        downheap(A, 0, j-1)

if __name__ == '__main__':
    print("Enter a sequence of numbers to sort: ")
    A = [int(i) for i in input().split()]
    heap_sort(A)
    print("Numbers after sorting: ")
    print(A)