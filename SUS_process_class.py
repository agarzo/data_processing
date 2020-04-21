# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:29:15 2019

@author: Ainara Garzo
"""

import csv
import easygui as eg
import statistics as stats

class SUS_quest:
    def __init__(self):
        self.csv_values = []
        
        self.open_csv()
        self.calculate_SUS()
    
    
    def open_csv(self):
        '''CSV format: first line with questions numbers
                        following lines with answers for each user'''
        
        extension = ["*.csv"]

        print "open the box"
        
        fileName = eg.fileopenbox(msg="Open File",
                                 title="Control: fileopenbox",
                                 default='',
                                 filetypes=extension)
        print "open the box2"
                       
        eg.msgbox(fileName, "fileopenbox", ok_button="Continuar")
        print "open the box3"
            
        with open(fileName) as File:
            reader = csv.reader(File, delimiter=',', quotechar=',',
                                quoting=csv.QUOTE_MINIMAL)
            for row in reader:
                self.csv_values.append(row)
    
    
    def calculate_SUS (self):
        results = [] 
        results2 = []
        
        for val in self.csv_values[1:len(self.csv_values)]:
            results.append(self.participant_SUS (val))
        
        
        for i in range (0, len(results)): 
            results2.append(results[i][1])
            print "The result for participant " + str (results[i][0]) + " is: " + str (results[i][1])
        
        final_result = self.mean (results2)
        print "The result of SUS questionnaires is: " + str(final_result)
    
    def participant_SUS (self, val_num):
        #SUS value calculation for each participant (using each row values)
        part_num, val_num = val_num[0].split(";", 1)

        val_num = val_num.replace(";", "")
        result = 0  
        
        i = 0      
    
        while i < len(val_num):
            result = result + (int (val_num[i])-1)
            result = result + (5-int (val_num[i+1]))
            
            i = i + 2
            
        result = result * 2.5
        return part_num, result
    
    def mean (self, SUS):
        #mean calculation for each participant's result
        return (stats.mean(SUS))

if __name__ == '__main__': 
      
    SUSQ = SUS_quest()