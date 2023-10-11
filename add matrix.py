# Function to add two matrices
def add_matrices(matrix1, matrix2):
    # Get the number of rows and columns in the matrices
    rows = len(matrix1)
    cols = len(matrix1[0])
    
    # Initialize a result matrix with zeros
    result = [[0 for _ in range(cols)] for _ in range(rows)]
    
    # Iterate through each element and add the corresponding elements
    for i in range(rows):
        for j in range(cols):
            result[i][j] = matrix1[i][j] + matrix2[i][j]
    
    return result

# Take input for the first matrix from the user
rows = int(input("Enter the number of rows for the matrices: "))
cols = int(input("Enter the number of columns for the matrices: "))

print("Enter elements for Matrix 1:")
matrix1 = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        row.append(element)
    matrix1.append(row)

# Take input for the second matrix from the user
print("Enter elements for Matrix 2:")
matrix2 = []
for i in range(rows):
    row = []
    for j in range(cols):
        element = int(input(f"Enter element at position ({i + 1}, {j + 1}): "))
        row.append(element)
    matrix2.append(row)

# Call the function to add matrices
result_matrix = add_matrices(matrix1, matrix2)

# Print the result
print("Matrix 1:")
for row in matrix1:
    print(row)

print("Matrix 2:")
for row in matrix2:
    print(row)

print("Resultant Matrix after Addition:")
for row in result_matrix:
    print(row)
