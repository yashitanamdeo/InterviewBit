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


    return 0

if __name__ == '__main__':
    main()