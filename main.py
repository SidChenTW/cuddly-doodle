import os
import sys

def AlwaysTrue():
    print ("AlwaysTrue()", end=' ')
    return True

def AlwaysFalse():
    print ("AlwaysFalse()", end=' ')
    return False
    

def int_test():
    print (bin(50))
    print (hex(50))
    print (oct(50))
    print (int('123'))
    print (int('111', 2))
    
    for i in range (-5, 5):
        print (i , round(9012345.678901, i))
    
    a = 255
    print (a.bit_length(), bin(a))
    print ((-255).bit_length(), bin(-255))
    
def bool_test():
    print ("AlwaysTrue() and AlwaysTrue()")
    if (AlwaysTrue() and AlwaysTrue()):
        pass
    print ()
    
    print ("AlwaysFalse() and AlwaysTrue()")
    if (AlwaysFalse() and AlwaysTrue()):
        pass
    print ()
    
    print ("AlwaysFalse() or AlwaysFalse()")
    if (AlwaysFalse() or AlwaysFalse()):
        pass
    print ()
    
    print ("AlwaysTrue() or AlwaysFalse()")
    if (AlwaysTrue() or AlwaysFalse()):
        pass
    print ()

def equal_float(a, b):
    return abs(a-b) <= sys.float_info.epsilon

def float_test():
    print ([0.0, 5.4, -2.5])
    print (sys.float_info.epsilon)

if __name__ == '__main__':
    int_test()
    bool_test()
    float_test()