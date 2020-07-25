# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:57:37 2020

@author: Ainara Garzo
"""

def get_file_name():
    while True:
        try:
            wfileName = input("Please enter a string for file name (include \"): ")
            if wfileName.find(".csv") < 1:
                wfileName = wfileName + ".csv"
            return wfileName
            break
        except ValueError:
            print("That was no valid name. Please, try again...")
        

def open_file(wfileName):
    outFile = open(wfileName, 'w')
    return outFile
    
def write_data_on_file(results, final_result, outFile):
    print results
    for item in enumerate (results):
        print item
        outFile.write(str(item[0]))
        outFile.write(";")
        outFile.write(str(item[1]))
        outFile.write("\n")
    outFile.write (str(final_result))
    outFile.close()
