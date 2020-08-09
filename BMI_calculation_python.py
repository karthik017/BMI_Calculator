# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 05:30:52 2020

@author: HP
"""

height = float(input("enter the height in metres:"))
weight = float(input("enter the weight in kg:"))

bmi = weight/(height**2)

print("your BMI is :{0} and you are :".format(bmi),end = ' ')

if(bmi < 16):
   print("severly underweight")
   
elif(bmi > 16 and bmi < 18.5):
    print("underweight")
    
elif(bmi >= 18.5 and bmi < 25):
    print("healthy")
elif(bmi >= 25 and bmi < 30):
    print("overweight")
    