# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 16:33:11 2025

@author: ashby
"""

def euclidean_process(num_1, num_2): #setting a function to find the gcd between 2 numbers

    def num_order(lower, higher): #function to set the order of the numbers
        if lower < higher:
            return lower, higher
        else:
            return higher, lower
        
    def get_remain(num1, num2): #function to find the remainder bewteen the two numbers
        remainder = num2%num1
        return remainder
    
    numb_1, numb_2 = num_order(num_1, num_2) #setting the order of the numbers
    
    if numb_1 == numb_2: #comparing if the numbers are the same
        return f"The greatest common divisor of {num_1} and {num_2} is {num_1}"
    elif numb_1 <= 0: #checking if the lower number is 0
        return f"There is no greatest common divisor between {numb_1} and {numb_2} is {numb_2}."
    else:
        while numb_1 != 0: #setting a loop to find the gcd
            remainder = get_remain(numb_1, numb_2) #finding the remainder of between the 2 numbers
            numb_2 = numb_1  #updating numb_2 to numb_1
            numb_1 = remainder  #updating numb_1 to the remainder
        return f"The greatest common divisor between {num_1} and {num_2} is {numb_2}"
            
    
    
num_1 = int(input("Please enter an integer: "))
num_2 = int(input("Please enter another integer: "))

print(euclidean_process(num_1, num_2))
    