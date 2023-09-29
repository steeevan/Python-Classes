# Problem 1

def caluclate_average(num1,num2):
    
    num1 = 2
    num2 = 45
    avg = (num1 + num2) / 2
    return avg  


print(caluclate_average(1, 2))


#problem 2

def Is_Even(n):
    if n == 0:
        return True
    elif (n==1):
        return False
    else:
        return Is_Even (n-2)
    
num = 33

if(Is_Even(num)):   
    print(num,"Is even")
else:
    print(num,"Is odd")


#problem 3

def factorial(x):
    if x == 1:
        return 1
    else:
        return(x *factorial(x-1))

num = 3

result = factorial(num)
print("The factorial of", num,"is", result)