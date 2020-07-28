# -*- coding: utf-8 -*-
"""
Created on Sat Jul 13 19:29:15 2019

@author: Ainara Garzo

Input --> csv format files:
- first line with questions or questions numbers (it is excluded of the process)
- first row with the users IDs: it is used to give the results for each user
- each user answers must be distributed in lines

Output --> csv format file: 
- one row with each user ID and SUS value
- last row with the mean value for all the users included in the input file

"""

import open_csv
import statistics as stats
import sus_values_class as svc
import write_on_file
import sys

class sus_quest:
    def __init__(self):
        self.csv_values = []
        self.wfileName = []
            
    def calculate_sus (self):

        pl = [] #participants data list
        srl =[] #sus scores result list
        
        for i,val in enumerate(self.csv_values):
            for x,item in enumerate(val.values):
                try:
                    self.csv_values[i].values[x] = int(self.csv_values[i].values[x])
                except ValueError:
                    print "The file has not the appropriated format"
                    return [], None
        
        for val in self.csv_values:
            id_num,values=self.participant_sus (val)
            sr = svc.sus_results(id_num,values)
            pl.append(sr)
        
        for item in pl: 
            srl.append(item.values)

        final_result = self.mean (srl)
        
        for item in pl:
            print "The result for participant " + str (item.id) + " is: " + str (item.values)
        print "The result of SUS questionnaires is: " + str(final_result)
        return pl, final_result
    
    def participant_sus (self, val_num):
        #SUS value calculation for each participant (using each row values)
        
        result = 0  
        
        i = 0      
    
        while i < len(val_num.values)-1:
            result = result + (int (val_num.values[i])-1)
            result = result + (5-int (val_num.values[i+1]))
            
            i = i + 2
            
        result = result * 2.5

        return val_num.id, result
    
    def mean (self, participants_values):
        #mean calculation for each participant's result
        return (stats.mean(participants_values))

if __name__ == '__main__':     
    SUSQ = sus_quest()
    try: 
        SUSQ.csv_values = open_csv.main()
        if SUSQ.csv_values != None:
            try: 
                SUSQ.wfileName = write_on_file.get_file_name()
                results, final_result = SUSQ.calculate_sus()
                out_file = write_on_file.open_file(SUSQ.wfileName)
                write_on_file.write_data_on_file(results, final_result, out_file)
            except:
                print "That was no valid name."
        else: print "There is not file selected or selected file has not appropriated format"
    except: 
        print "There is not file selected or selected file has not appropriated format"
        
    