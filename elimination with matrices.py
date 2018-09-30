import numpy as np #import moudule for  work with numpy (matrices)

def elimination(a, b, c, d, e, f, h, g, k): #create function which take elements of matrix
    matrix = np.zeros((0,3)) #create matrix with all rows = 0 and 3 colunns
    matrix = np.concatenate((matrix, [[a, b, c], [d, e, f], [h, g, k]])) #add our arguments as elements of matrix
    
    if a == 0: #do condition
        matrix = np.concatenate((matrix, [[d, e, f], [a, b, c], [h, g, k]])) #switch rows when the first element of matrix is equal to 0
        print(d) #print d as first element of elimination
        if d == 0:
            matrix = np.concatenate((matrix, [[h, g, k], [d, e, f], [a, b, c]]))
            if h == 0:
                print('Matrix is Singular.', 'Look at row 1-column 1, row 2-column 1 and row 3- column 1')
                print('Right now will be an error. Dont worry.')
    else: 
        if a < d and a < h: #for d and h in elimination
           result_of_a = -(d // a) #find the pivot for 'a' which converts the first column (besides first element of first column)
           result_2_of_a = -(h // a) #find the pivot for 'a' which converts the first column (besides first element of first column)
           
           zero_d = result_of_a + a  
           new_e = result_of_a + b #add the result to find the second row of the matrix
           new_f = result_of_a + c
           
           zero_h = result_2_of_a + h #create 0 in position letter 'h'
           
           matrix = np.concatenate((matrix, [[a, b, c], [zero_d, new_e, new_f], [zero_h, g, k]])) #write the new matrix 
           print(a)
    if  new_e == 0: #do condition
        matrix = np.concatenate((matrix, [[zero_d, new_e, new_f], [a, b, c], [zero_h, g, k]])) #switch rows when the second element of matrix is equal to 0
        print(h) #print new as the second element of elemination
        if b == 0:
            print('Matrix is Singular.', 'Look at row 1-column 2, row 2-column 2 and row 3- column 2')
    else:
        if new_e < g: 
            result_of_new_e = -(g // new_e)
            
            new_g = result_of_new_e + new_e
            new_k = result_of_new_e + new_f
            
            matrix = np.concatenate((matrix, [[a, b, c], [zero_d, new_e, new_f], [zero_h, new_g, new_k]]))
            print('', new_e, ' \n', new_k)
elimination(0, 3, 0, 0, 7, 0, 0, 7, 1)
