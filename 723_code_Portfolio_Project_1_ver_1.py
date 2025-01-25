# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 15:30:22 2025

@author: ashby
"""

def euclidean_process(num_1, num_2): #setting a function to find the gcd between 2 numbers
    def get_remain(lower, higher): #nested function to find the remainder bewteen the two numbers
        remainder = higher%lower
        return remainder    
    if num_1 == num_2: #comparing if the numbers are the same
        return f"The greatest common divisor of {num_1} and {num_2} is {num_1}"
    elif num_1 <= 0 or num_2 <= 0: #comparing if either number is 0
        return f"There is no greatest common divisor between {num_1} and {num_2}."
    else:
        while True:
            number_1 = num_1 #reasigning the numbers for the loop
            number_2 = num_2
            if number_1 == 0: #ending the loop once we find the gcd
                return f"The greatest common divisor between {num_1} and {num_2} is {number_1}."
            elif number_1 < number_2: #comparing if number_1 is lower than number_2
                lower = number_1
                higher = number_2
                remainder = get_remain(lower, higher) #getting the remainder for the two numbers
                number_1 = remainder #reasigning to the updated numbers
                number_2 = lower #reasigning to the updated numbers
            else: 
                lower = number_2
                higher = number_1
                remainder = get_remain(lower, higher) #getting the remainder for the two numbers
                number_1 = remainder #reasigning to the updated numbers
                number_2 = lower #reasigning to the updated numbers
                
            
    
    
num_1 = int(input("Please enter an integer: "))
num_2 = int(input("Please enter another integer: "))

print(euclidean_process(num_1, num_2))
    