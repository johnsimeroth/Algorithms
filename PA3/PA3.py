#cd Desktop/"Personal items"/Software/algorithms/PA3

import random

# def MedianOf3(A,ArraySize):
#     if ArraySize <= 2:
#         px = 0
#         return px
#     else:
#         f = A[0]
#         if ArraySize % 2 == 0:
#             idx2 = ArraySize//2-1
#             m = A[idx2]
#         else:
#             idx2 = ArraySize//2
#             m = A[idx2]
#         l = A[-1]
#         idx = [0, idx2, -1]
#         fml = [f,m,l]
#         mini = min(fml)
#         maxi = max(fml)
#         for i in range(0,3):
#             if fml[i] > mini and fml[i] < maxi:
#                 med = fml[i]
#                 px = idx[i]
#         return px

# def MedianOf3(A,ArraySize):
#     if ArraySize <= 2:
#         px = 0
#         return px
#     else:
#         f = A[0]
#         idx2 = ArraySize//2 + ArraySize%2 - 1
#         m = A[idx2]
#         l = A[-1]
#         idx = [0, idx2, -1]
#         fml = [f,m,l]
#         mini = min(fml)
#         maxi = max(fml)
#         for i in range(0,3):
#             if fml[i] > mini and fml[i] < maxi:
#                 med = fml[i]
#                 px = idx[i]
#         return px

def MedianOf3(A,ArraySize):
        f = A[0]
        idx2 = ArraySize//2 + ArraySize%2 - 1
        m = A[idx2]
        l = A[-1]

        # make tuples, then sort by the 2nd value of each (index = 1),
        # then pull the middle value of the sorted 3 (index = 1),
        # then pull the original idx of that value (1st part of tuple, index = 0)
        fml = [(0,f),(idx2,m),(-1,l)]
        px = sorted(fml, key = lambda fml_val: fml_val[1])[1][0]
        return px

def SelectPivot(A,ArraySize,mode):
    if mode == 'first':
        px = 0
    elif mode == 'middle':
        px = ArraySize//2
    elif mode == 'last':
        px = ArraySize-1
    elif mode == 'med3':
        px = MedianOf3(A,ArraySize)
    elif mode == 'random':
        px = random.randint(0,ArraySize - 1)
    else:
        print(f''' \n\n\n OOPS! You tried using a mode that's \n
            undefined. Check spelling and capitalization, please!''')
    return px


def PartitionArray(A,mode):
    i = 1
    n = len(A)
    px = SelectPivot(A,n,mode)
    p = A[px]
    A[0], A[px] = p, A[0]
    for j in range(1,n):
        if A[j] < p:
            A[i], A[j] = A[j], A[i]
            i += 1
    px = i - 1
    A[0], A[px] = A[px], A[0]
    return A, px

def QuickSort(A,c,mode):
    if len(A) <= 1:
        return A, c
    else:
        A, px = PartitionArray(A,mode)
        x = len(A[:px])
        if x > 1:
            c += x - 1
        A[:px], c = QuickSort(A[0 : px], c, mode)
        y = len(A[px+1:])
        if y > 1:
            c += y - 1
        A[px+1:], c = QuickSort(A[px+1 ::], c, mode)
        return A, c

def ReadArray(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            lines.append(int(line))
    return lines
print(f'\n \n \n \n \n \n')
TestArray = ReadArray('QuickSortArray.txt')
mode = ['first', 'last', 'med3']

for x in mode:
    A, c = QuickSort(TestArray[:],len(TestArray)-1,x)
    print(f'\n number of comparisons = {c}')
