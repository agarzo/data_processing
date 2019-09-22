# -*- coding: utf-8 -*-
"""
Created on Sun Jul 21 10:10:02 2019

@author: Ainara Garzo
"""

import numpy as np
#import numbers

def media ():
#    values = values.replace('\t', '')
#    values = values.replace('\n', '')
#    values = values.replace(' ' , '')
    val_num = np.array([])
    
    value = raw_input()
#    value = value.replace('\t', '')
#    value = value.replace('\n', '')
#    value = value.replace(' ' , '')
#    print value
    while isinstance(value, float) or isinstance(value, int):
#    while value != '\n' or value != ' ':
        print value    
        
        val_num = np.insert(val_num, 0 , value)
        value = raw_input()
#        value = value.replace('\t', '')
#        value = value.replace('\n', '')
#        value = value.replace(' ' , '')
        print value
    return np.mean(val_num)


if __name__ == '__main__': 
    print "Write the SUS values separated by enter"
    result = media()
    print "result is: " + str(result)