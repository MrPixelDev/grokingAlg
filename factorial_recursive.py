def factorial(num: int) -> int:
  fact = 1;
  if (num > 0):
    fact = num * factorial(num - 1);
  return fact;

print(factorial(5));

def fact(x: int) -> int:
  if (x == 1):
    return 1;
  else:
    return x * fact(x-1);
  
print(fact(7));