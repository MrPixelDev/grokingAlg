
def qsort(arr):
  if (len(arr) < 2):
    return arr;
  else:
    base = arr[0];
    less = [i for i in arr[1:] if i < base];
    greater = [i for i in arr[1:] if i >= base];
    return qsort(less) + [base] + qsort(greater);
  


print(qsort([3, 10, 2, 44, 15, 3, -3, 3, -3]))