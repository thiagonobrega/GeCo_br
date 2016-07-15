'''
Created on 12 de abr de 2016

@author: Thiago
'''
import os
import random
import sys
import time
sys.path.append('..')
import attrgenfunct

if __name__ == '__main__':
    
    for i in range(1,100):
        #print attrgenfunct.generate_normal_date(1, 31 , 3, 4 , 2016 , 2016)
        print attrgenfunct.generate_normal_datetime(1, 31 , 1, 12 , 2014, 2016)
    
    