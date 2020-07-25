# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:29:15 2019

@author: Ainara Garzo

This script reads CSV format files:
- first line with questions or questions numbers (it is excluded of the process)
- first row with the users IDs: it is used to give the results for each user
- each user answers must be distributed in lines

"""

import open_csv
import statistics as stats
import write_on_file

class SUS_quest:
    def __init__(self):
        self.csv_values = []
        self.wfileName = []
            
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
        return results2, final_result
    
    def participant_SUS (self, val_num):
        #SUS value calculation for each participant (using each row values)
        part_num, val_num = val_num[0].split(";", 1)

        val_num = val_num.replace(";", "")
        result = 0  
        
        i = 0      
    
        while i < len(val_num)-1:
#            print ("i: " + str(i) + " val_num: " + str(len(val_num)))
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
    SUSQ.csv_values = open_csv.main()
    SUSQ.wfileName = write_on_file.get_file_name()
    if SUSQ.csv_values != None:
        results2, final_result = SUSQ.calculate_SUS()
        out_file = write_on_file.open_file(SUSQ.wfileName)
        write_on_file.write_data_on_file(results2, final_result, out_file)
    else: pass