#!/usr/bin/python3

name = 'Joe'
lastname = 'Doe'
age = 23

grades = [-12, 22, 89, 50, -95, 34]

print ("My name is %s, %s and my age is %d!" % (lastname, name, 21)) 

print ("print alligned") 
for grade in grades:
    print("%3d" % +grade)

print ("print filled with zeros") 
for grade in grades:
    print("%03d" % +grade)    
    