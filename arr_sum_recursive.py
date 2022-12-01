
def summ(arr):
  x = 0;
  if (len(arr) == 0):
    return x;
  # elif (len(arr) == 1): any of theese
    # return arr.pop(0); 
  else:
    return x + arr.pop(0) + summ(arr);


print(summ([5, 2, 3, 4]));