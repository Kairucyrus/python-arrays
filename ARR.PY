# -*- coding: utf-8 -*-
"""
Created on Fri Mar 17 19:08:57 2023

@author: Kairu Cyrus
"""
import numpy as np
a = np.linspace(1, 12, num=10) #linspace(start, stop,num(optional), 
                  #           endpoint(boolean,optional),retstep(boolean,optional))
                  
#print(a)
x= np.arange(2,28,2)
#i = np.array(12)
#print(np.ndim(k)) #returns number of dimensions of the array
k= np.array([ [1,5,6,7,8,9,12,14,24,73],
               [34,45,87,75,47,45,56,89,62,46],
               [50,79,41,13,17,29,33,64,28,91]])
print(k[1:, :]) # Slicing the multidimensional array  
                #returns [[34 45 87 75 47 45 56 89 62 46]
                #         [50 79 41 13 17 29 33 64 28 91]]
                # from second to end rows 
                #in a nut shell, slicing k[y:,:l] would return elements from the 
                # y*th row, first column to last row last column
#print(k.ndim)
#print(np.shape(k)) # returns (3,9), the shape of the array(rows,columns)
#k.shape=(2,15)  
#print(k)
                # returns [[ 1  5  6  7  8  9 12 14 24 73 34 45 87 75 47]
                #          [45 56 89 62 46 50 79 41 13 17 29 33 64 28 91]]
                #size of original array equals size of new array(number of 
                #elements equal) otherwise,
                #throws an error ValueError: cannot reshape array of size 27 into shape(x,y)
                
#u=k[1]
#print(k[6]) #k[1,6] returns same value  #returns the seventh(index 6) element
                                        # in the second row(k[1])
print(k[:, 8:])   #only returns elements in the ninth and tenth columns for all rows



a = np.linspace(1, 12, num=10)
#print(a)
x= np.arange(2,28,2)
#Slicings bring a distinction between list and tuples (on one side) and arrays
# Slicing an array creates a view on the original array while the same operation
# leads to creation of new items as for tuples and lists
j= np.array([1,2,3,4,5,6,7,8,9])
l= j[2:7]
l[0] = 11
l[4]= 28
print(j) #returns [ 1  2 11  4  5  6 28  8  9]
p=[1,2,3,4,5,6,7,8,9]
s=p[1:5]
s[0]= 13
s[3]=29
print(p)   #prints [1, 2, 3, 4, 5, 6, 7, 8, 9]
