import numpy as np

import numpy as np 

#CREATING ARRAY 
#1d array 
arr1 = np.array([1,2,3,4])
print (arr1)

#2d array 
arr2 = np.array(([1,2,3,4],[5,6,7,8]))
print(arr2)

#ARRAY ATTRIBUTES
print(arr2.shape)
print(arr2.dtype)
print(arr2.size)

#BASIC ARRAY OPERATIONS
arr3 = np.array([5,6,7,8])
print(arr3)
#ADDITION 
print(arr3+arr1)
#MULTIPLICATION 
print(arr3*arr1)

#ARRAY SLICING AND INDEXING 
#slicing 1d array 
print(arr1[1:3])
print(arr2[0,1])#first row and second column

#GENERATING ARRAYS 
arr4 = np.arange(0,10,2)
print(arr4)#evenly spaced values where the dis will be 2
arr_zeros = np.zeros((2,3))#will make a zero matrix with two rows and 3 columns
print(arr_zeros)
arr_ones = np.ones((2,2))
print(arr_ones)
arr_linespace = np.linspace(0,1,5)
print (arr_linespace)

#RESHAPING ARRAY 
arr5 = np.arange(1,10)
arr_reshaped = arr5.reshape(3,3)
print(arr_reshaped)

#STATISTICAL FUNCTIONS
arr6 = np.array([1,2,3,4,5,6,7,8,9])
#mean
print(np.mean(arr6))
print(np.median(arr6))
print(np.sum(arr6))
print(np.min(arr6),np.max(arr6))

ran_num = np.random.random()
rand_int = np.random.randint(1,10,size=(3,3))
print(rand_int)

#BROADCASTING 
arr7 = np.array([1,2,3])
arr8 = np.array([[1],[2,],[3]])
print (arr7+arr8)

"""DICE ROLL SIMULATOR"""
roll = np.random.randint(1,7,size= (1000,2))
sums = roll.sum(axis=1)

unique, counts = np.unique(sums, return_counts=True)
print(dict(zip(unique,counts)))

"""TEMPRETURE CONVERTER"""
user_input = input('enter tempreture in celcius (seprated by spaces):')
#split the input string into a lot of strings
temp_string = user_input.split()
#converting into array 
celciuus = np.array(temp_string, dtype=float)
fehranite = (celciuus*9/5)+32
print(f"tempreture in fehranite:{fehranite}")