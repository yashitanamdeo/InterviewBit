'''Problem Statement:https://www.interviewbit.com/problems/string-validators/'''

def main():
    S = input()
    #Your code goes here
    alnum = False
    alpha = False
    digit = False
    lower = False
    upper = False

    for i in S:
        if i.isalnum():
            alnum = True
        if i.isalpha():
            alpha = True
        if i.isdigit():
            digit = True
        if i.islower():
            lower = True
        if i.isupper():
            upper = True
    print(alnum,alpha,digit,lower,upper, sep="\n")

    #Alternate Method
    '''
    print("True" if any(i.isalnum() for i in S) else "False")
    print("True" if any(i.isalpha() for i in S) else "False")
    print("True" if any(i.isdigit() for i in S) else "False")
    print("True" if any(i.islower() for i in S) else "False")
    print("True" if any(i.isupper() for i in S) else "False")
    
    '''


    return 0

if __name__ == '__main__':
    main()