#!/usr/bin/python

def my_function(par):    #Note the colon (:)
    a = 2 * par     
    return a         
    
def my_other_function(par):
    a = 100 * my_function(par)     
    return a 
    
def get_name():
    name = raw_input("What is your name? ")     
    return name 
    
    