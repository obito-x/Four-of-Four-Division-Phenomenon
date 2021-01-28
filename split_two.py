# Divisor or Factor Caculation
import sys


def split_two(num):
	for i in range(1, num+1):
	    test = num - i
	    if(test >= i):
	    	yield (test ,i)
	    else:
	    	break
if __name__ == '__main__':
    if(len(sys.argv) >= 2):
        num = int(sys.argv[1])
        for i, j in split_two(num):
            print(i,j)
