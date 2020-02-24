import os
import sys

def data_test():
    print (bin(50))
    print (hex(50))
    print (oct(50))
    print (int('123'))
    print (int('111', 2))
    
    for i in range (-5, 5):
        print (i , round(9012345.678901, i))
        
    
if __name__ == '__main__':
    data_test()