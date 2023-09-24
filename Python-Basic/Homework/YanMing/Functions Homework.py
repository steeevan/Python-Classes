#Problem 1
def caculate_average(num1,num2):
    summ = num1 + num2
    return summ/2
answer = caculate_average(132,381)
print(answer)
#Problem 2
def is_even(num):
    if num%2 == 0:
        print("true")
    else:
        print("false")
is_even(4)
#Problem 3
def caculate_factorial(n):
    number = 1
    for i in range(2, n+1):
        number *= i
    return number


answer = caculate_factorial(12)
print(answer)
