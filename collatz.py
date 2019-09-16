#   The number we will perform the collatz operations on
n = 20

#   Keep looping until we reach 1
while n !=1:
    #   Print current value of n
    print(n)
    #   Check if n is even
    if n % 2 == 0:
        #   If n is even, divide by 2
        n = n/2
    else:
        #   If odd, multiply by 3 and add 1
        n = (3*n) + 1


print(n)
