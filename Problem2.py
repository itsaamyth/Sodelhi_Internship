def diagonalDifference(arr,n):
    leftdiagonal = 0
    rightdiagonal = 0

    for i in range(0,n):
        leftdiagonal = leftdiagonal+arr[i][i]
        rightdiagonal = rightdiagonal+arr[i][n-i-1]
    return abs(leftdiagonal-rightdiagonal)
    
arr=[[1,2,3],[4,5,6],[9,8,9]]
n=3
print("Diagonal Difference :",diagonalDifference(arr,n))
