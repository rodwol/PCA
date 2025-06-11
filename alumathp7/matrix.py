def multiply(A, B):
    """  matrix manipulation library that handles multiplication """
    # Check if A and B are lists of lists
    if not all(isinstance(row, list) for row in A) or not all(isinstance(row, list) for row in B):
        raise TypeError("Both matrices must be lists of lists")

    # Check if all rows in A and B have the same length
    if len(set(len(row) for row in A)) > 1 or len(set(len(row) for row in B)) > 1:
        raise ValueError("All rows in both matrices must have the same length")

    # Check dimension compatibility
    if len(A[0]) != len(B):
        raise ValueError("Number of columns in A must equal number of rows in B")

    result = [[0 for _ in range(len(B[0]))] for _ in range(len(A))]

    for i in range(len(A)):
        for j in range(len(B[0])):
            for k in range(len(B)):
                result[i][j] += A[i][k] * B[k][j]
    return result
