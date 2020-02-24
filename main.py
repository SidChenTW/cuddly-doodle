import math
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
    
    a = 123.456
    print (int(a))
    print (round(a, 1))
    print (math.floor(a))
    print (math.ceil(a))
    a = 12.0
    print (a.is_integer())
    b = 4.125
    print (b.as_integer_ratio())
    
    s = b.hex()
    print (s)
    print (float.fromhex(s))
    
    print (math.pi)
    print (math.hypot(5, 12))
    print (math.modf(13.732))

if __name__ == '__main__':
    int_test()
    bool_test()
    float_test()