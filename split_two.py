# Divisor or Factor Caculation
import sys


# 
#	   +------------+
#	   | 	   40- 19   =  21 ------------------+
#	   | 	        |	    |			        |
#	   | 	(9+10)<-+		+-> (18+19)         |
#	   | 	  					 			    |
#      | 	 				 			        |    
#      | 					    			    |					  
# [(i, 19-i) for i in range(1,19+1)]	  [(i, 21-i) for i in range(1,21+1)]
#	   |										|
#  (if 19-i >= i)					       (if 21-i >= i)



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
