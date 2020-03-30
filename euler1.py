def main():
  """
  If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9.
  The sum of these multiples is 23.

  Find the sum of all the multiples of 3 or 5 below 1000.
  """
  test()
  print(do_the_thing(1000))

def do_the_thing(target):
  numbers = range(1, target)
  answer = []

  for i in numbers:
      #print(i)
      if is_multiple_of(i, 3) or is_multiple_of(i, 5):
          answer.append(i)
      #ends here => i won't be a thing after this

  return(sum(answer))

def test():
  result = do_the_thing(10)

  if result == 23:
    print("success")
    print(result)
  else:
    print("check again pinhead")
    print(result)
    
def is_multiple_of(num, multiple):
  #print("is_multiple_of")
  return num % multiple == 0

main()