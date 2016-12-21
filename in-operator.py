#!/usr/bin/python

def membership( first ):
    print ('first: ',first, ', id:', id(first))
    list = [1, 2, 3, 4, 5 ]

    if ( first in list ):
       print ("Line 1 - a is available in the given list")
    else:
       print ("Line 1 - a is not available in the given list")
   
def identity( first, second ):
    print ('first: ',first, ', id:', id(first), 'second: ',second, ', id:', id(second))

    if ( first is second ):
       print ("Line 2 - a and b have same identity")
    else:
       print ("Line 2 - a and b do not have same identity")   