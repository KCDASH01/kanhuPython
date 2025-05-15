numb=int(input('Enter a number: '))
def Factorial(a):
    if a<2:
        return 1
    else:
        return a * Factorial(a-1)
result= Factorial(numb)
print(f'Factorial of {numb} is: ', result)