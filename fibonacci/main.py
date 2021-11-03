def fib(n):
    if n < 2:
        return 1
    return fib(n-2) + fib(n-1)

def main():
    number = int(input())
    print(fib(number-1))

if __name__ == "__main__":
    main()
