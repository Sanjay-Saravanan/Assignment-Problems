# Function to demonstrate printing pattern triangle
def triangle(n):
    # number of spaces
    k = 0

    # outer loop to handle number of rows
    for i in range(4):

        # inner loop to handle number spaces
        # values changing acc. to requirement
        for j in range(0, n):
            print("*", end=" ")

        # decrementing k after each loop
        k = k - 1

        # inner loop to handle number of columns
        # values changing acc. to outer loop
        for j in range(0):
            # printing stars
            print("*", end="")

        # ending line after each row
        print("\r")


# Driver Code
n = 4
triangle(n)