'''Problem Statement:https://www.interviewbit.com/problems/list-comprehensions/'''

def main():
    str_list = ['given', 'intern', 'InterviewBit', 'network', 'local', 'multiple', 'define', 'nodes', 'algorithm', 'allows', 'community', 'phase', 'single']
    my_list = []
    for i in str_list:
        if len(i) % 2 != 0:
            my_list.append(i)
        else:
            continue
    print(my_list)
    return 0

if __name__ == '__main__':
    main()