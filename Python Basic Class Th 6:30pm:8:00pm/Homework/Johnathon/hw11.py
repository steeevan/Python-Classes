#7-8

def logger(func):
  def wrapper():
    print (f"logging function {func.__name__}")
    return func()
  return wrapper

#1-2
@logger
def apply_operation():
  return 1+2
print (apply_operation())

#don't know 3-4

#5-6

# I used an input function so type in 2 for the number and
# 5 for the power
def power(a):
  b=int(input("enter a power"))
  print (f"{a} to the power of {b} is equal to {a**b}")
power(a=int(input("enter a number")))




