'''Problem Statement:https://www.interviewbit.com/problems/loops-and-jump-statements/'''

def main():
    N = int(input())
    # YOUR CODE GOES HERE
    for i in range(N):
        if i%2!=0:
            print(i)
        else:
            continue
        

    return 0

if __name__ == '__main__':
    main()