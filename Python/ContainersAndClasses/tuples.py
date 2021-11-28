'''Problem Statement:https://www.interviewbit.com/problems/tuples/'''

def main():
    tuple1 = tuple(("one", "two", "three"))
    tuple2 = tuple(("1", "2", "3"))
    
    # change value at index 0 of both tuple to string "number"
    # Your code goes here
    list1 = list(tuple1)
    list2 = list(tuple2)

    list1[0] = 'number'
    list2[0] = 'number'

    tuple1 = tuple(list1)
    tuple2 = tuple(list2)

    print(tuple1)
    print(tuple2)
    
    return 0

if __name__ == '__main__':
    main()