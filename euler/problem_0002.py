# Even Fibonacci numbers

# Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the
# first 10 terms will be:
#
# 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#
# By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the
# even-valued terms.

import sys

def fib(n):
    a, b, fib_list = 1, 2, []
    while a < n:
        fib_list.append(a)
        a, b = b, a + b

    return fib_list

def main():
    args = sys.argv
    if len(args) == 2 and args[1].isdigit():
        param = int(args[1])
    else:
        param = 10

    fib_nums = fib(param)
    print(sum(fib_nums[i] for i in range(0, len(fib_nums)) if fib_nums[i] % 2 == 0))

if __name__ == '___main__':
    main()