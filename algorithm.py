#!/usr/bin/python3
# This program is only for debugging purpose
import sys


def algorithm(aList, verbose=False, print_result=False):

    # All possible Caculation(adding or subtracting) between four number pair

    # eg. a + b
    adding_two_pair = [tuple(aList[i:2+i]) for i in range(len(aList)-1)]
    # eg. a + b + c
    adding_three_pair = [tuple(aList[i:3+i]) for i in range(len(aList)-2)]
    # eg. a + b + c - d
    one_minus_four_pair = []
    # eg. a + c -b -d
    two_minus_four_pair = []
    # eg. a - c
    one_minus_two_pair = []
    # eg. b + c - d
    one_minus_three_pair = []
    # eg. a -d -c
    two_minus_three_pair = []
    # eg. a -b -c -d
    three_minus_four_pair = []
    # result
    result = []



    # Adding Two Pair
    for i in range(2, 4):
        adding_two_pair += [tuple(aList[j::i]) for j in range(len(aList)-i)]

    # Adding Three Pair
    adding_three_pair  += [tuple(aList[0:2] + [aList[3]])]
    adding_three_pair += [tuple(aList[0::2] + [aList[3]])]

    # One Minus Four Pair
    for i in range(4):
        temp = aList.copy()
        temp[i] = temp[i]*(-1)
        one_minus_four_pair += [tuple(temp)]

    # Two Minus Four Pair
    for x, y in adding_two_pair:
        temp = aList.copy()
        temp[temp.index(x)] = x*(-1)
        temp[temp.index(y)] = y*(-1)
        two_minus_four_pair += [tuple(temp)]

    # One Minus Two Pair
    for num in aList:
        one_minus_two_pair += [(num, i*(-1)) for i in aList if num != i]



    # One Minus Three Pair
    for t_pair in adding_two_pair:
        for num in aList:
            if num not in t_pair:
                one_minus_three_pair += [tuple(list(t_pair) + [num*(-1)])]


    # Two Minus Three Pair
    for i in aList:
        tempList = aList.copy()
        tempList = [item*(-1) for item in tempList]
        tempList.pop(aList.index(i))
        two_minus_three_pair += [tuple([i] + tempList[:2])]
        two_minus_three_pair += [tuple([i] + tempList[::2])]
        two_minus_three_pair += [tuple([i] + tempList[1:3])]

    # Three Minus Four Pair
    for i in range(4):
        temp = aList.copy()
        temp = [item*(-1) for item in temp]
        temp[i] = temp[i]*(-1)
        three_minus_four_pair += [tuple(temp)]


    if(verbose):
        print("adding_four_pair_list: ", aList)
        print("adding_two_pair_list: ", adding_two_pair)
        print("adding_three_pair_list: ", adding_three_pair)
        print("one_minus_four_pair_list: ", one_minus_four_pair)
        print("two_minus_four_pair_list: ", two_minus_four_pair)
        print("one_minus_two_pair_list: ", one_minus_two_pair)
        print("one_minus_three_pair_list: ", one_minus_three_pair)
        print("two_minus_three_pair_list: ", two_minus_three_pair)
        print("three_minus_four_pair_list: ", three_minus_four_pair)
        

        print("sumof_adding_four_pair: ", sum(aList))
        print("sumof_adding_two_pair: ", [sum(i) for i in adding_two_pair])
        print("sumof_adding_three_pair: ", [sum(i) for i in adding_three_pair])
        print("sumof_one_minus_four_pair: ", [sum(i) for i in one_minus_four_pair])
        print("sumof_two_minus_four_pair: ", [sum(i) for i in two_minus_four_pair])
        print("sumof_one_minus_two_pair: ", [sum(i) for i in one_minus_two_pair])
        print("sumof_one_minus_three_pair: ", [sum(i) for i in one_minus_three_pair])
        print("sumof_two_minus_three_pair: ", [sum(i) for i in two_minus_three_pair])
        print("sumof_three_minus_four_pair: ", [sum(i) for i in three_minus_four_pair])
        


    # Total all together
    result += [sum(i) for i in adding_two_pair]
    result += [sum(i) for i in adding_three_pair]
    result += [sum(i) for i in one_minus_four_pair]
    result += [sum(i) for i in two_minus_four_pair]
    result += [sum(i) for i in one_minus_two_pair]
    result += [sum(i) for i in one_minus_three_pair]
    result += [sum(i) for i in two_minus_three_pair]
    result += [sum(i) for i in three_minus_four_pair]
    result += [sum(aList)]
    result += aList


    # Sort the result
    result.sort()

    if(print_result):
        print("(unset) len: " ,len(result))
        print("(unset) result: ", result)

    # Uniq the result
    result = list(set(result))

    if(print_result):
        print("(set) len: ", len(result))
        print("(set) result: ", result)


    return result


def _usage():
    print(f"\nUsage: python3 {sys.argv[0]} <four pair of number>")
    print(f"eg. python3 {sys.argv[0]} 13 11 9 7\n")
    sys.exit()


if __name__ == '__main__':
    # Only For StandAlone Caculation or Debugging
    if(len(sys.argv) == 5):
        aList = []
        for s in sys.argv[1:6]:
            if(s.isnumeric):
                aList.append(int(s))
            else:
                _usage()
        algorithm(aList, verbose=True, print_result=True)
    else:
        _usage()

