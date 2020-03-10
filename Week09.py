# (1) First line: Determine the number of Row and Column, separated by a space
#
# (2) Second line: Number of bookings
#
# (3) Following lines: Booking positions to be specified by Row and Column indices
#
# Steps:
#
# Start with a 2D list with the size specified in (1) where all elements initialized to zeros ('0')
# If the requested booking position is available, then take the booking (by incrementing variable success by 1), and update the availability in the list (by setting the booking position to 1).
# If the requested booking position is not available, then increment variable failure by 1.
# Output format:
#
# (1) Mark each booked position with ‘X’ and an available position with ‘_’
#
# (2) Print the total numbers of successful and failed bookings.


# n : number of rows
# m : number of columns
# seat : 2d list for keeping track of all bookings
# success : number of successes
# failure : number of failures

success = failure = 0
n, m = map(int, input().split())
seat = [[0]*m for _ in range(n)]

for _ in range(int(input())):
    x, y = map(int, input().split())
    if seat[x][y]:
        failure += 1
    else:
        seat[x][y] = 1
        success += 1



for i in range(n):
    for j in range(m):
        if seat[i][j] == 1:
            print("X", end = " ")
        else:
            print("_", end = " ")
    print()
print("Success={}, Failure={}".format(success, failure))