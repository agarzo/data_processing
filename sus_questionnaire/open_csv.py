# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:11:25 2020

@author: Ainara Garzo

open csv files and include the data in 'csv_values' structure.
use browser for selecting the appropriate csv file.
"""

import csv
import easygui as eg
import sus_values_class as svc
import sys

def main():
    
    fileName = open_window()
    if fileName == None or fileName.find(".csv") < 1: 
        exit
    else: return open_csv(fileName)

def open_window():
    
    #open browser to select the .csv file containing the data to be processed
    extension = ["*.csv"]
    
    fileName = eg.fileopenbox(msg="Open File",
                             title="Control: fileopenbox",
                             default='',
                             filetypes=extension)
                   
    eg.msgbox(fileName, "fileopenbox", ok_button="Continue")
    
    return fileName

def open_csv(fileName):
    
    csv_values = []
    
    #open the csv file giving the corresponding fileName string
    #include the values in the csv_values structure
    with open(fileName) as File:
        reader = csv.reader(File, delimiter=';', quotechar=',', 
                            quoting=csv.QUOTE_MINIMAL)
        
        first_row = reader.next() #exclude first row - questions numbers
        i=0
        for row in reader:
            if len(first_row) == 11:
                sv = svc.sus_values(row[0])
                sv.add_values(row[1:len(row)])
            elif len(first_row) == 10:
                sv = svc.sus_values("ID"+i)
                sv.add_values(row)
            else: 
                print "There is not file selected or selected file has not appropriated format"
                sys.exit()
            i=i+1       
            csv_values.append(sv)

    #check if any value is missing an substute for '3' according to Bangor et al., 2009
    for i,item in enumerate(csv_values):
        for x,y in enumerate(item.values):
            if y == '':
                csv_values[i].values[x] = 3
        
    return csv_values