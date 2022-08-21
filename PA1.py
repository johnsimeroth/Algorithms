

#cd desktop/"Personal Items"/software/algorithms/PA1
num1 = "3141592653589793238462643383279502884197169399375105820974944592"
num2 = "2718281828459045235360287471352662497757247093699959574966967627"
#num1 = "12345678"
#num2 = "56789123"

def factorial(x):
    if x == 1:
        return 1
    else:
        return (x * factorial(x-1))

# num = 6
# print(factorial(num))

def rev_str(str):
    # This method takes in a string and reverses it
    return str[::-1]

def ten_one_split(x):
    # This method takes an INT and splits it into ones and tens
    # For example, 15 -> tens = 1, ones = 5.
    # Return is a string list
#test
    ones = "0"
    tens = "0"
    if x < 10:
        tens = "0"
        ones = str(x)
    else:
        tens = str(x)[0]
        ones = str(x)[1]
    return [tens, ones]

def grade_school(x1,x2):

    ones = "0"
    tens = "0"
    row = ["0"]

    for idx, i in enumerate(reversed(x2)):
        for j in reversed(x1):
            prod_sum = int(i) * int(j) + int(tens)
            [tens, ones] = ten_one_split(prod_sum)
            row[idx] += ones
        row[idx] += tens
        row.append("0")
    row.pop(idx+1)

    for idx, i in enumerate(row):
        row[idx] = row[idx][1:]
        row[idx] = "0" * idx + row[idx]

    digits = len(max(row, key = len))

    for idx, i in enumerate(row):
        row[idx] = rev_str(rev_str(row[idx]).zfill(digits))

    ones = "0"
    tens = "0"
    x = 0
    sum = "0"

    for i in range(digits):
        for j in row:
            x += int(j[i])
        [tens, ones] = ten_one_split(x + int(tens))
        sum += ones
        x = 0
    sum += tens
    sum = sum[1:]
    product = rev_str(sum).lstrip("0")
    return product

def splitStr(x1,x2):
    # ADD CHECK FOR ODD LENGTHS
    #print(f'splitStr input: {x1}, {x2} ')
    x1Len = len(x1)
    x2Len = len(x2)
    a = x1[0 : x1Len//2]
    b = x1[x1Len//2 : x1Len]
    c = x2[0 : x2Len//2]
    d = x2[x2Len//2 : x2Len]
    #print(f'splitStr output: {a}, {b}, {c}, {d}')
    return [a, b, c, d]

def karatsuba(x1,x2):
    #step 0: break x1 (ab) and x2 (cd) in half: a,b, and c,d
    #step 1: multiply the first halves of each (a*c)
    #step 2: multiply the second halves of each (b*d)
    #step 3: multiply (a+b)*(c+d)
    #step 4: compute [3] - [2] - [1]
    #step 5: 10^n * [1] + 10^(n/2) * [4] + [2]
    #print(f'karatsuba input: {x1}, {x2}')
    if len(x1) == 1 or len(x2) == 1:
        #print('x1 length == 1')
        return str(int(x1) * int(x2))
    else:
        [a,b,c,d] = splitStr(x1,x2)
        S1 = karatsuba(a,c)
        S2 = karatsuba(b,d)
        S31 = int(a) + int(b)
        S32 = int(c) + int(d)
        #S3 = karatsuba(str(S31),str(S32))
        S3 = S31 * S32
        S4 = int(S3) - int(S2) - int(S1)
        S5 = 10 ** len(x1) * int(S1) + 10 ** (len(x1)//2) * S4 + int(S2)
        return str(S5)

import time
print(f'\n \n \n')
start = time.perf_counter()
answer = grade_school(num1,num2)
end = time.perf_counter()
print(f'The product of \n {num1} \n and \n {num2} \n is \n {answer}')
print(f'It took {end - start} to compute')
# FIGURE OUT WHY GRADESCHOOL METHOD IS OFF

print(f'\n')
start = time.perf_counter()
answer2 = karatsuba(num1,num2)
end = time.perf_counter()
print(f'The kProduct of \n {num1} \n and \n {num2} \n is \n {answer2}')
print(f'It took {end - start} to compute')
# MAKE KARATSUBA A LITTLE MORE HONEST
# BREAK OUT ADDITION STEPS BY INDIVIDUAL DIGITS
# ADD HANDLING FOR UNEVEN DIGIT COUNTS
# MAKE THE S3 MULTIPLICATION RECURSIVE
# ADD HANDLING FOR UNEQUAL X1 AND X2 LENGTHS (BREAK OFF FIRST CHUNK AND MULTIPLY BY 10^?)

realAns = str(int(num1) * int(num2))
print(realAns)
print(f'Is gradeSchool correct? {realAns == answer}')
print(f'Is kProduct correct? {realAns == answer2}')
