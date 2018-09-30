"""
//// Rustam Silin//////
"""
import numpy as np 

def elimination(a, b, c, d, e, f, h, g, k): #elements of matrix (3x3)
    matrix = np.zeros((0,3))
    matrix = np.concatenate((matrix, [[a, b, c], [d, e, f], [h, g, k]])) 
    
    if a == 0: #do row exchange
        matrix = np.concatenate((matrix, [[d, e, f], [a, b, c], [h, g, k]])) 
        print(d)
        if d == 0:
            matrix = np.concatenate((matrix, [[h, g, k], [d, e, f], [a, b, c]])) #do again row exchange
            if h == 0: #if have all zeroes in first column
                print('Matrix is Singular.', 'Look at row 1-column 1, row 2-column 1 and row 3- column 1')
                print('Right now will be an error. Dont worry.')
    else: 
        if a < d and a < h: 
           result_of_a = -(d // a) #find the multiplier for 2,1 position
           result_2_of_a = -(h // a) #for 3,1 position
           
           zero_d = result_of_a + a #new 2,1 position (zero) 
           new_e = result_of_a + b #2,2
           new_f = result_of_a + c #2,3
           
           zero_h = result_2_of_a + h #zero (3,1 position) 
           
           matrix = np.concatenate((matrix, [[a, b, c], [zero_d, new_e, new_f], [zero_h, g, k]])) #convert the matrix
           print(a) #print 1 pivot
    
    if  new_e == 0: 
        matrix = np.concatenate((matrix, [[zero_d, new_e, new_f], [a, b, c], [zero_h, g, k]])) 
        print(h)
        if b == 0:
            print('Matrix is Singular.', 'Look at row 1-column 2, row 2-column 2 and row 3- column 2')
    else:
        if new_e < g: 
            result_of_new_e = -(g // new_e)
            
            new_g = result_of_new_e + new_e
            new_k = result_of_new_e + new_f
            
            matrix = np.concatenate((matrix, [[a, b, c], [zero_d, new_e, new_f], [zero_h, new_g, new_k]])) #convert to the final matrix
            print('', new_e, ' \n', new_k)
elimination(0, 3, 0, 0, 7, 0, 0, 7, 1) #for example (output error)
