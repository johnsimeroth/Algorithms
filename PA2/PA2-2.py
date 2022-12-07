#cd desktop/"Personal Items"/software/algorithms/PA2
# 0. MergeSort
# 1. CountInv

def SplitArray(array):
    n = len(array)
    Array1 = array[:n//2]
    Array2 = array[n//2:]
    return [Array1,Array2]

def CountInversions(A): #input type: Array of ints
    # Base Case
    if len(A) == 1:
        inversions = 0
        return [A,inversions]
    else:
        # Split
        [B,C] = SplitArray(A)
        # print(f'B = {B}')
        # print(f'C = {C}')
        # Sort
        [B, x] = CountInversions(B)
        [C, y] = CountInversions(C)

        # Merge
        i = 0
        j = 0
        z = 0
        n = len(A)
        SortedArray = [0] * n
        # print(f'n = {n}')
        for k in range(n):
            # print(f'k = {k}')
            # print(f'i = {i}')
            # print(f'j = {j}')
            if i >= len(B):
                SortedArray[k] = C[j]
                z += len(B) - i
                j += 1
            elif j >= len(C):
                SortedArray[k] = B[i]
                i += 1
            else:
                if B[i] <= C[j]:
                    SortedArray[k] = B[i]
                    i += 1
                else:
                    SortedArray[k] = C[j]
                    z += len(B) - i
                    j += 1
        # print(f'D = {D}')
        inversions = x + y + z
        return [SortedArray,inversions]

def ReadArray(filename):
    lines = []
    with open(filename) as file:
        while (line := file.readline().rstrip()):
            lines.append(int(line))
    return lines

TestArray = ReadArray('InversionCountArray.txt')
# TestArray = [8, 1, 3, 5, 2, 4, 6]
[sorted,inversions] = CountInversions(TestArray)

print(f'\n \n {TestArray} \n \n sorted is \n \n {sorted} \n')
print(f'There are {inversions} inversions')
