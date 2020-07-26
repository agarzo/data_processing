# -*- coding: utf-8 -*-
"""
Created on Sun Jul 26 10:09:17 2020

@author: Ainara Garzo
"""

class sus_values:
    #structure used for saving the data from the csv files and to process
    def __init__(self, i):
        self.id = i
        self.values = []    # creates a new empty list for each participant

    def add_values(self, items):
        self.values=items
        
        
class sus_results:
    #structre used for the results obtained after the sus process

    def __init__(self, i, result):
        self.id = i
        self.values = result