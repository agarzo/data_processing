# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:11:25 2020

@author: Ainara Garzo
"""

import csv
import easygui as eg

def main():
    
    fileName = open_window()
    if fileName == None or fileName.find(".csv") < 1: 
        print "There is not file selected or selected file is not a csv."
    else: return open_csv(fileName)

def open_window():
    
        
    extension = ["*.csv"]
    
    fileName = eg.fileopenbox(msg="Open File",
                             title="Control: fileopenbox",
                             default='',
                             filetypes=extension)
                   
    eg.msgbox(fileName, "fileopenbox", ok_button="Continue")
#    print fileName
    
    return fileName

def open_csv(fileName):
    
    csv_values = []
#    print fileName            
    with open(fileName) as File:
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            csv_values.append(row)
#    print csv_values
    return csv_values