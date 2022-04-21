"""
Find apartments with Ocean view 

Input = Array of integers that represent the height of apartments. Left most apartment is in index 0 & the array lists the apartments from left to right. After the rightmost apartment, we hit the ocean. Apartments are of the same width and in a straight line from left to right towards the ocean.
Output = Take in the Array and return the indexes of the apartments that have ocean view

// Ocean View
//Input: [4, 3, 2, 3, 1]
//Output: [0, 3, 4]
//
//   ___ 
// 4 |  |  ___         ___
// 3 |  |  |  |  ___   |  |
// 2 |  |  |  |  |  |  |  |  ___
// 1 |  |  |  |  |  |  |  |  |  |
//                               ~~~~~ Ocean
//   b0,    b1,   b2,   b3,   b4
"""
import numpy as np

def ocean_view_finder (apts: np.array) -> np.array:

    ocean_view_apts = np.array([])

    for i in range(len(apts)):
        print(ocean_view_apts)

        if i == len(apts) - 1 :
            ocean_view_apts = np.concatenate((ocean_view_apts, np.array([int(i)])), axis = 0)
        elif apts[i] > apts[i+1:].max():
            ocean_view_apts = np.concatenate((ocean_view_apts, np.array([int(i)])), axis = 0)
        else:
            continue

    return ocean_view_apts

print(ocean_view_finder(np.array([4, 3, 2, 3, 1])))