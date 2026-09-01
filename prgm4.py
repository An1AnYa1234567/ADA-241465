''' Program-4: WAP to implement strassen_multiply(A: List[List[int]], 
B: List[List[int]]) -> List[List[int]] accepting two N×N matrices and returning their product matrix.'''
# Strassen Matrix Multiplication
# Using Divide and Conquer
def strassen_multiply(A, B):
    n = len(A)
    # Base case: if matrix is 1 x 1
    if n == 1:
        return [[A[0][0] * B[0][0]]]
    # Find the middle point
    mid = n // 2
    # Divide matrix A into 4 parts
    A11 = [row[:mid] for row in A[:mid]]
    A12 = [row[mid:] for row in A[:mid]]
    A21 = [row[:mid] for row in A[mid:]]
    A22 = [row[mid:] for row in A[mid:]]
    # Divide matrix B into 4 parts
    B11 = [row[:mid] for row in B[:mid]]
    B12 = [row[mid:] for row in B[:mid]]
    B21 = [row[:mid] for row in B[mid:]]
    B22 = [row[mid:] for row in B[mid:]]
    # Helper function for matrix addition
    def add(X, Y):
        return [
            [X[i][j] + Y[i][j] for j in range(len(X))]
            for i in range(len(X))
        ]
    # Helper function for matrix subtraction
    def subtract(X, Y):
        return [
            [X[i][j] - Y[i][j] for j in range(len(X))]
            for i in range(len(X))
        ]
    # Calculate the 7 Strassen products
    M1 = strassen_multiply(add(A11, A22), add(B11, B22))
    M2 = strassen_multiply(add(A21, A22), B11)
    M3 = strassen_multiply(A11, subtract(B12, B22))
    M4 = strassen_multiply(A22, subtract(B21, B11))
    M5 = strassen_multiply(add(A11, A12), B22)
    M6 = strassen_multiply(subtract(A21, A11), add(B11, B12))
    M7 = strassen_multiply(subtract(A12, A22), add(B21, B22))
    # Calculate the four parts of the result matrix
    C11 = add(subtract(add(M1, M4), M5), M7)
    C12 = add(M3, M5)
    C21 = add(M2, M4)
    C22 = add(subtract(add(M1, M3), M2), M6)
    # Combine the four parts into one matrix
    C = []
    for i in range(mid):
        C.append(C11[i] + C12[i])

    for i in range(mid):
        C.append(C21[i] + C22[i])

    return C
# Example
A = [
    [1, 2],
    [3, 4]
]

B = [
    [5, 6],
    [7, 8]
]
# Call the function
result = strassen_multiply(A, B)
# Display the result
print("Result:")
for row in result:
    print(row)