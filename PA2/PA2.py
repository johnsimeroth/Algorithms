#cd desktop/"Personal Items"/software/algorithms/PA2
# 0. MergeSort
# 1. CountInv

def SplitArray(array):
    n = len(array)
    Array1 = array[:n//2]
    Array2 = array[n//2:]
    return [Array1,Array2]

def MergeSort(A): #input type: Array of ints
    # Base Case
    if len(A) == 1:
        return A
    else:
        # Split
        [B,C] = SplitArray(A)
        # print(f'B = {B}')
        # print(f'C = {C}')
        # Sort
        B = MergeSort(B)
        C = MergeSort(C)

        # Merge
        i = 0
        j = 0
        n = len(A)
        D = [0] * n
        # print(f'n = {n}')
        for k in range(n):
            # print(f'k = {k}')
            # print(f'i = {i}')
            # print(f'j = {j}')
            if i > len(B) - 1:
                D[k] = C[j]
                j += 1
            elif j > len(C) - 1:
                D[k] = B[i]
                i += 1
            else:
                if B[i] <= C[j]:
                    D[k] = B[i]
                    i += 1
                else:
                    D[k] = C[j]
                    j += 1
        # print(f'D = {D}')
        return D

def ReadArray(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            lines.append(int(line))
    return lines

TestArray = ReadArray('InversionCountArray.txt')
sorted = MergeSort(TestArray)

print(f'\n \n {TestArray} \n sorted is \n {sorted} \n')
