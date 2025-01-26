# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 12:41:46 2025

@author: ashby
"""


def euclidean_process(num_1, num_2): #setting a function to find the gcd between 2 numbers

    def pos_num(number1, number2): #function to make all negative inputs positive
        if number1 < 0 and number2 < 0: #if both numbers are negative
            pos_num_1 = number1*(-1) #multiply the number by -1 to make it positive
            pos_num_2 = number2*(-1) #multiply the number by -1 to make it positive
            return pos_num_1, pos_num_2 #returning the 2 positive numebrs
        elif number1 < 0 and number2 >= 0: #checking if the first number is negative
            pos_num_1 = number1*(-1) 
            return pos_num_1, number2
        elif number2 < 0 and number1 >= 0: #checking if the second number is negative
            pos_num_2 = number2*(-1)
            return pos_num_2, number1
        else:
            return number1, number2 #if both are positive, leave them as is
    
    def num_order(lower, higher): #function to set the order of the numbers
        if lower < higher: #if the first number is lower
            return lower, higher #return the values in order from lowest to highest
        else:
            return higher, lower #return the values in order from lowest to highest
        
    def get_remain(num1, num2): #function to find the remainder bewteen the two numbers
        remainder = num2%num1 #finding the remainder of the 2 numbers
        return remainder
        
    while True: #setting a loop to ensure the 2 inputs are integer
        try:
            #converting the 2 numbers to integers
            num1 = int(num_1)
            num2 = int(num_2)
            
            pos_1, pos_2 = pos_num(num1, num2) #making both inputs positive
            numb_1, numb_2 = num_order(pos_1, pos_2) #setting the order of the numbers
                
            if numb_1 == numb_2: #comparing if the numbers are the same
                return f"The greatest common divisor of {num_1} and {num_2} is {numb_1}"
            elif numb_1 == 0: #checking if the lower number is 0
                return f"There is no greatest common divisor between {num_1} and {num_2} is {numb_2}."
            else:
                while numb_1 != 0: #setting a loop to find the gcd
                    remainder = get_remain(numb_1, numb_2) #finding the remainder of between the 2 numbers
                    numb_2 = numb_1  #updating numb_2 to numb_1
                    numb_1 = remainder  #updating numb_1 to the remainder
                return f"The greatest common divisor between {num_1} and {num_2} is {numb_2}"
        
        except ValueError: #if an error occurs, prompt the user to enter 2 integers
            print ("The input requires two integers. Please try again.")
            num_1 = input("First Number: ")
            num_2 = input("Second Number: ")
                
            
    
    
num_1 = input("Please enter an integer: ")
num_2 = input("Please enter another integer: ")

print(euclidean_process(num_1, num_2))
    