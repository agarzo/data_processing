# -*- coding: utf-8 -*-
"""
Created on Sat Jul 25 10:11:25 2020

@author: Ainara Garzo

open csv files and include the data in 'csv_values' structure.
use browser for selecting the appropriate csv file.
"""

import csv
import easygui as eg

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
        reader = csv.reader(File, delimiter=',', quotechar=',',
                            quoting=csv.QUOTE_MINIMAL)
        for row in reader:
            csv_values.append(row)

    return csv_values