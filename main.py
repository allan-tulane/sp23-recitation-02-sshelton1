"""
CMPS 2200  Recitation 2
"""

### the only imports needed are here
import tabulate
import time
import math
###

def simple_work_calc(n, a, b):
  """Compute the value of the recurrence $W(n) = aW(n/b) + n

	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor

	Returns: the value of W(n).
	"""
	# TODO
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return a * simple_work_calc(n//b, a, b) + n

def test_simple_work():
	""" done. """
	assert simple_work_calc(10, 2, 2) == 36
	assert simple_work_calc(20, 3, 2) == 230
	assert simple_work_calc(30, 4, 2) == 650
  #Additional Tests
	assert simple_work_calc(20, 3, 3) == 56
	assert simple_work_calc(30, 4, 3) == 182
	assert simple_work_calc(40, 5, 3) == 330

def work_calc(n, a, b, f):
  """Compute the value of the recurrence $W(n) = aW(n/b) + f(n)
  
	Params:
	n......input integer
	a......branching factor of recursion tree
	b......input split factor
	f......a function that takes an integer and returns 
           the work done at each node 

	Returns: the value of W(n).
	"""
  # TODO
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return a * work_calc(n//b, a, b, f) + f(n)

def span_calc(n, a, b, f):
  """Compute the span associated with the recurrence $W(n) = aW(n/b) + f(n)
    
  Params:
  n......input integer
  a......branching factor of recursion tree
  b......input split factor
  f......a function that takes an integer and returns 
          the work done at each node 

  Returns: the value of W(n).
  """
	# TODO
  if n == 0:
    return 0
  elif n == 1:
    return 1
  else:
    return span_calc(n//b, a, b, f) + f(n)
  

def test_work():
  """ done. """
  assert work_calc(10, 2, 2, lambda n: 1) == 15 #TODO
  assert work_calc(20, 1, 2, lambda n: n*n) == 530 #TODO
  assert work_calc(30, 3, 2, lambda n: n) == 300 #TODO
  """"Additional Test"""
  assert work_calc(20, 3, 3, lambda n: n*n) == 544
  assert work_calc(30, 2, 3, lambda n: n) == 70
  assert work_calc(40, 4, 3, lambda n: 1) == 85

def compare_work(work_fn1, work_fn2, work_fn3, sizes=[10, 20, 50, 100, 1000, 5000, 10000]):
  """
	Compare the values of different recurrences for 
	given input sizes.

	Returns:
	A list of tuples of the form
	(n, work_fn1(n), work_fn2(n), ...)
	"""
  
  result = []
  for n in sizes:
    #compute W(n) using current a, b, f
    result.append((n, work_fn1(n), work_fn2(n), work_fn3(n)))
  return result

def print_results(results):
  """ done """
  print(tabulate.tabulate(results,
  headers = ['n', 'W_1', 'W_2', 'W_3'],
  floatfmt = ".3f",
  tablefmt = "github"))

def test_compare_work():
  def work_fn1(n):
    return work_calc(n, 2, 2, lambda n: n**(math.log(2, 2) - 1))

  def work_fn2(n):
    return work_calc(n, 2, 2, lambda n: n**(math.log(2, 2) + 1))

  def work_fn3(n):
      return work_calc(n,2,2, lambda n: n**(math.log(2, 2)))
 
  res = compare_work(work_fn1, work_fn2, work_fn3)
  print_results(res)

def test_compare_span():
  def work_fn1(n):
    return work_calc(n, 2, 2, lambda n: n**(math.log(2, 2) - 1))

  def work_fn2(n):
    return work_calc(n, 2, 2, lambda n: n**(math.log(2, 2) + 1))

  def work_fn3(n):
      return work_calc(n,2,2, lambda n: n**(math.log(2, 2)))
 
  res = compare_work(work_fn1, work_fn2, work_fn3)
  print_results(res)

#Work Information
print("Work:\n")
print("f(n) = 1")
print(work_calc(10, 2, 2, lambda n: 1))
print(work_calc(20, 2, 2, lambda n: 1))
print(work_calc(30, 2, 2, lambda n: 1))
print(work_calc(40, 2, 2, lambda n: 1))
print(work_calc(50, 2, 2, lambda n: 1))
print(work_calc(60, 2, 2, lambda n: 1))
print(work_calc(70, 2, 2, lambda n: 1))
print("\n")

print("f(n) = log(n)")
print(work_calc(10, 2, 2, lambda n: math.log(n)))
print(work_calc(20, 2, 2, lambda n: math.log(n)))
print(work_calc(30, 2, 2, lambda n: math.log(n)))
print(work_calc(40, 2, 2, lambda n: math.log(n)))
print(work_calc(50, 2, 2, lambda n: math.log(n)))
print(work_calc(60, 2, 2, lambda n: math.log(n)))
print(work_calc(70, 2, 2, lambda n: math.log(n)))
print("\n")

print("f(n) = n")
print(work_calc(10, 2, 2, lambda n: n))
print(work_calc(20, 2, 2, lambda n: n))
print(work_calc(30, 2, 2, lambda n: n))
print(work_calc(40, 2, 2, lambda n: n))
print(work_calc(50, 2, 2, lambda n: n))
print(work_calc(60, 2, 2, lambda n: n))
print(work_calc(70, 2, 2, lambda n: n))

#Span Calculation

print("\nSpan:\n")
print("f(n) = 1")
print(span_calc(10, 2, 2, lambda n: 1))
print(span_calc(20, 2, 2, lambda n: 1))
print(span_calc(30, 2, 2, lambda n: 1))
print(span_calc(40, 2, 2, lambda n: 1))
print(span_calc(50, 2, 2, lambda n: 1))
print(span_calc(60, 2, 2, lambda n: 1))
print(span_calc(70, 2, 2, lambda n: 1))
print("\n")

print("f(n) = log(n)")
print(span_calc(10, 2, 2, lambda n: math.log(n)))
print(span_calc(20, 2, 2, lambda n: math.log(n)))
print(span_calc(30, 2, 2, lambda n: math.log(n)))
print(span_calc(40, 2, 2, lambda n: math.log(n)))
print(span_calc(50, 2, 2, lambda n: math.log(n)))
print(span_calc(60, 2, 2, lambda n: math.log(n)))
print(span_calc(70, 2, 2, lambda n: math.log(n)))
print("\n")

print("f(n) = n")
print(span_calc(10, 2, 2, lambda n: n))
print(span_calc(20, 2, 2, lambda n: n))
print(span_calc(30, 2, 2, lambda n: n))
print(span_calc(40, 2, 2, lambda n: n))
print(span_calc(50, 2, 2, lambda n: n))
print(span_calc(60, 2, 2, lambda n: n))
print(span_calc(70, 2, 2, lambda n: n))

print("\nCompare Work")
test_compare_work()

print("\nCompareSpan")
test_compare_span()