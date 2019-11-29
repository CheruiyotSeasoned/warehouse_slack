# recursive program to find the fibonacci of a number
#not efficient for finding the nth fib number of a large input n. say 100.
def fib(n):
    if n < 0:
        print("incorrect input")
    elif n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)


# n = 100 input takes 10 plus minutes to produce an output nth fib.
print(fib(int(input("Enter a number to find its Fibonnaci:"))))