'''Problem Statement:https://www.interviewbit.com/problems/functions/'''

#Return the factorial of the number N
def factorial(N):
    # Your code goes here
    fact = 1
    for i in range(1,N+1):
        fact*=i
    return fact