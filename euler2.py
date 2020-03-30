def main():
    """
    Each new term in the Fibonacci sequence is generated by adding the previous two terms.
    By starting with 1 and 2, the first 10 terms will be:

    1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

    By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
    """
    #here
    print(make_fib(4000000))
  

def test():
    desired = 44
    actual = make_fib(100)
    if desired == actual:
      print("hooray")
    else:
        print("boo")
        print(actual)

def make_fib(n):
    answer = 0
    fib = [1,1]
      
    while fib[-1] <= n:
        if is_even(fib[-1]):
            answer += fib[-1]
        fib.append(sum(fib[-2:]))

    return answer

def is_even(num):
    #print("is_multiple_of")
    return num % 2 == 0

main()