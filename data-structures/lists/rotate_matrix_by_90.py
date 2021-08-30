#!python3

# rotate a 2 dimensional array(matrix) by 90 degree

def rotate_matrix(matrix):
    print(matrix)
    # Create transpose
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):

            matrix[i][j] = matrix[j][i]

    # swap elements
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            temp = matrix[i][j]
            matrix[i][j] = matrix[]

    print(matrix)


if __name__ == '__main__':
    input_matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    rotate_matrix(input_matrix)
