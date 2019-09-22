# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:29:15 2019

@author: Ainara Garzo
"""
    
def calculate_SUS (val):

    val_num = val.replace('\t', '')
    val_num = val_num.replace(' ' , '')
    result = 0  
    i = 0      

    while i < len(val_num):
        result = result + (int (val_num[i])-1)
        result = result + (5-int (val_num[i+1]))
        i = i + 2
        
    result = result * 2.5
    return result

if __name__ == '__main__': 
    print "Write the SUS values separated by blanks"
    SUS_values = raw_input()
    result = calculate_SUS (SUS_values)
    print "SUS result is: " + str(result) + "%"