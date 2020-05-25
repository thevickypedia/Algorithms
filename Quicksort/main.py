# Quick Sort
# ! /usr/bin/env python3
import random

noComp = 0


def partition(A, l, r):
    global noComp
    pivot = A[l]
    i = l + 1
    for j in range(l + 1, r + 1):
        noComp += 1
        if A[j] < pivot:
            A[j], A[i] = A[i], A[j]
            i += 1
    A[l], A[i - 1] = A[i - 1], A[l]
    return i - 1


def qsort(A, l, r, vers):
    if l < r:
        prepareArray(A, l, r, vers)
        partitionIndex = partition(A, l, r)
        qsort(A, l, partitionIndex - 1, vers)
        qsort(A, partitionIndex + 1, r, vers)


def prepareArray(A, l, r, vers):
    if vers == "median3":
        a = A[l]
        c = A[r]
        mid = int((l + r) / 2)
        b = A[mid]
        li = [a, b, c]
        li.sort()
        if li[1] == b:
            A[l], A[mid] = A[mid], A[l]
        elif li[1] == c:
            A[l], A[r] = A[r], A[l]
    elif vers == "random":
        ra = random.randint(l, r + 1)
        A[l], A[ra] = A[ra], A[l]


fileName = input('Please enter a filename:\n')
variant = input('Please enter a Quicksort variant:\n')

with open(fileName) as f:
    content = f.readlines()
content = [x.strip() for x in content]
content = [int(x) for x in content]
noComp = 0
qsort(content, 0, len(content) - 1, variant)
print(noComp)
