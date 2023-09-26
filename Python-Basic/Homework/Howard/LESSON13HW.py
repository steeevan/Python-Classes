print("WELCOME TO Howard's Homework")
def calculate_avarage(num1,num2):
    calopyodia = ((num1+num2)/2)
    return calopyodia



def is_even(number):
    if number % 2 == 1:
        return False
    else:
        return True



def calculate_factorial(num):
    n = 1
    for i in range(1,int(num + 1)):
        n = i * n
    return n
