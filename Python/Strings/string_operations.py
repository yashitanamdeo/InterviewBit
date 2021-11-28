'''Problem Statement:https://www.interviewbit.com/problems/string-operations/'''

def main():
    S = input()
    
    #Print length of the string S
    print(len(S))
    
    #Print the first occurence of the letter 'a' in S
    #Note it is guaranteed that letter a is present in the string S
    print(S.index("a"))

    #Print all the characters with even index in S
    print(S[::2])
    return 0

if __name__ == '__main__':
    main()