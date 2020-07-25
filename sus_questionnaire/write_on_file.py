# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 15:57:37 2020

@author: Ainara Garzo

open a csv file and writting the results on it
"""

def get_file_name():
    
    #request a name to create a new csv file and get from the keyboard input
    #the fileName must be declared as string including ""
    wfileName = input("Please enter a string for output file name (include \" \" on the name): ")
    if wfileName.find(".csv") < 1:
        wfileName = wfileName + ".csv"
    return wfileName        

def open_file(fileName):
    #create a writable file giving a fileName
    outFile = open(fileName, 'w')
    return outFile
    
def write_data_on_file(results, final_result, outFile):
    
    #write the results on the csv and close the file
    for item in (results):
        outFile.write(str(item[0]))
        outFile.write(";")
        outFile.write(str(item[1]))
        outFile.write("\n")
    outFile.write ("mean;"+str(final_result))
    outFile.close()
