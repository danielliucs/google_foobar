def solution(n):
    # Your code here
    matrix = [[0 for _ in range(n+1)] for __ in range(n+1)]
    matrix[0][0] = 1

    for staircase in range(1, n+1):
        for left_partition in range(n+1):
            matrix[staircase][left_partition] = matrix[staircase-1][left_partition]
            if left_partition >= staircase:
                matrix[staircase][left_partition] += matrix[staircase-1][left_partition-staircase]
    return matrix[n][n]-1


print(solution(3))
print(solution(200))
print(solution(6))
print(solution(8))