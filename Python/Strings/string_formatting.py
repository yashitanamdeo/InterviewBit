'''Problem Statement:https://www.interviewbit.com/problems/string-formatting/'''

def main():
    data = ("Robin", 10, "chocolates")
    format_string = None
    print("Hello {0}. You are currently left with {1} {2}.".format(data[0],data[1],data[2]))
    #print(f"Hello{data[0]}. You are currently left with {data[1]} {data[2]}.)  --> fstring
    return 0

if __name__ == '__main__':
    main()