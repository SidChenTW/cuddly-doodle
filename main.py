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

def complex_test():
    import cmath
    z = 5-12j
    print(z.real, z.imag)
    print (z.conjugate())
    
def decimal_test():
    import decimal
    a = decimal.Decimal(9876)
    b = decimal.Decimal("54321.012345678987654321")
    print (a + b)
    c = decimal.Decimal.from_float(1.234)
    print (c)
    
    print (23/1.05)
    print (decimal.Decimal(23)/decimal.Decimal('1.05'))

def string_test():
    text='''HelloWorld
1.2.3.4.5
6.7.8.9.10'''
    print (text)
    a = '"---" \'---\''
    b = "\"---\" '---'"
    print (a)
    print (b)
    s = r"\\\r\n"
    print (s)

    s = "1234" + \
        "5678"
    print (s)
    
    s = ("12345"
         "67890")
    print (s)

    euros = "€ \N{euro sign} \u20AC \U000020AC"
    print (euros)
    
    print (ord(euros[0]))
    print (hex(ord(euros[0])))
    
    s = chr(8734), chr(0x23b7)
    
    print (s)
    print (ascii(s))
    
def unicode_test():
    import unicodedata
    print (chr(0x00c5))
#    unicodedata.normalize()
#   unicode collation Algorithm

    print (unicodedata.lookup('LEFT CURLY BRACKET'))
    print (unicodedata.name('/'))
    print (unicodedata.decimal('9'))
    print (unicodedata.category('A'))
    print (unicodedata.bidirectional('\u0660'))
    

def slice_test():
    s = "ABCDEFGHIJ"
    for i in range(-10, 10):
        print (i, s[i])
    
    print(s[:])
    print(s[0:len(s)])
    print(s[::])
    print(s[0:len(s):1])
    print(s[::-1])
    print(s[-1:-len(s)-1:-1])
    
    print (s[::-2])
    print (s[-2::-2])
    
    #
    # str.join()
    #
    data = ['1', '2', '3', '4', '5']
    print (' '.join(data))
    print ('.'.join(data))
    print (' --> '.join(data))    
    
    print (' '.join(reversed(data)))
    print (' '.join(data[::-1]))
    
def string_method_test():
    s = 'hello world'
    print (s.capitalize())
    print ('98765432109876543210')
    print (s.center(20, ' '))
    print (s.center(20, '-'))
    print (s.count('l', 3, -1))
    print (s.count('ll'))
    
    text = "hello world, python!!"
    print (text.capitalize(), text.capitalize().istitle())
    print (text.title(), text.title().istitle())
    
    print (text.center(40, '-'))
    print (text.center(40))
    print (text.ljust(100, '*'))
    print (text.rjust(100, '*'))
#    print (text.format())
    print (s.count('l'))
    print (s.count('ll'))
    
    a = 'aeiou'
    b = '12345'
    table = ''.maketrans(a, b)
    print ('aueoi'.translate(table))
    
def string_format_test():
    print ("The novel '{0}' was published in {1}".format("Hard Times", 1854))
    
    print ("The novel '{{{0}}}' was published in {1}".format("Hard Times", 1854))
    
    # {field_name}
    # {field_name!conversion}
    # {field_name:format_specification}
    # {field_name!conversion:format_specification}
    
    print ("{who} turned {age} this year.".format(who='She', age=88))
    print ("The {who} was {0} last week.".format(12, who="boy"))
    
    stock = ["paper", "envelopes", "notepads", "pens", "paper clips"]
    print ("We have {0[1]} and {0[2]} in stock".format(stock))
    
    d = dict(animal='elephants', weight=12000)
    print ("The {0[animal]} weight {0[weight]} kg.".format(d))
    
    import math, sys
    print ("math.pi=={0.pi} sys.maxunicode=={1.maxunicode}.".format(math, sys))
    
    element = "Silver"
    number = 47
    print ("Elephant {number} is {element}.".format(**locals()))
    
    import decimal
    print ("{0} {0!s} {0!r} {0!a}".format(decimal.Decimal("93.4")))
    
    print ("{0} {0!s} {0!r} {0!a}".format("翻訳する"))
    
    s = "The sword of truth."
    print ("{0}".format(s))
    print ("{0:25}".format(s))
    print ("{0:>25}".format(s))
    print ("{0:^25}".format(s))
    print ("{0:-^25}".format(s))
    print ("{0:.<25}".format(s))
    print ("{0:.10}".format(s))
    
    maxwidth = 12
    print ("{0}".format(s[:maxwidth]))
    print ("{0:.{1}}".format(s, maxwidth))
    
    print ("{0:0=12}".format(8749203))
    print ("{0:0=12}".format(-8749203))
    
    print ("{0:012}".format(8749203))
    print ("{0:012}".format(-8749203))
    
    print ("{0:*<15}".format(8749203))
    print ("{0:*>15}".format(8749203))
    print ("{0:*^15}".format(8749203))
    print ("{0:*^15}".format(-8749203))

    print ("[{0:}][{1:}]".format(539802, -539802))
    print ("[{0: }][{1: }]".format(539802, -539802))
    print ("[{0:+}][{1:+}]".format(539802, -539802))
    print ("[{0:-}][{1:-}]".format(539802, -539802))

    print ("{0:b} {0:o} {0:x} {0:X}".format(14613198))
    print ("{0:#b} {0:#o} {0:#x} {0:#X}".format(14613198))

    print ("{0:,} {0:*>13,}".format(int(2.39432185e6)))

    import locale
    locale.setlocale(locale.LC_ALL, "")
    x, y = (1234567890, 1234.56)
    locale.setlocale(locale.LC_ALL, "C")
    c = "{0:n} {1:n}".format(x, y)
    print (c)

    locale.setlocale(locale.LC_ALL, "en_US.UTF-8")
    en = "{0:n} {1:n}".format(x, y)
    print (en)
    
    locale.setlocale(locale.LC_ALL, "de_DE.UTF-8")
    de = "{0:n} {1:n}".format(x, y)
    print (de)

    amount = (10 ** 3) * math.pi
    print ("[{0:12.2e}] [{0:12.2f}]".format(amount))
    print ("[{0:*>12.2e}] [{0:*>12.2f}]".format(amount))
    print ("[{0:*>+12.2e}] [{0:*>+12.2f}]".format(amount))
    
    print ("{:,.6f}".format(decimal.Decimal("1234567890.1234567890")))
    print ("{:,.6}".format(decimal.Decimal("1234567890.1234567890")))

    print ("{0.real:.3f}{0.imag:+.3f}j".format(4.75917+1.2042j))
    print ("{0.real:.3f}{0.imag:+.3f}j".format(4.75917-1.2042j))

    print ("{0:,.4f}".format(3.59284e6-8.984327843e6j))



if __name__ == '__main__':
    int_test()
    bool_test()
    float_test()
    complex_test()
    decimal_test()
    string_test()
    unicode_test() #??
    slice_test()
    string_method_test()
    string_format_test()