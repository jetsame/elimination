import numpy as np 

def elim(a, b, c, d, e, f, g, h, k): #matrix 3x3 (abc def ghk)
    matrix = np.zeros((0, 3))
    matrix = np.concatenate((matrix, [[a, b, c], [d, e, f], [g, h, k]])) 

    elements = a, b, c, d, e, f, g, h, k
    if elements == 0:
        assert 'Matirx is full zeros' #if all matrix is zero

    elif a > d and g: 
        p_d = -(d / a)
        r_d = p_d * (a) + d 
        r_e = p_d * (b) + e
        r_f = p_d * (c) + f

        p_g = -(g / a)
        r_g = p_g * (a) + g
        matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, h, k]]))

        p_re = -(h / r_e)
        r_h = p_re * (r_e) + h
        r_k = p_re * (r_f) + k

        matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, r_h, r_k]]))
        print('1:', a, int(r_e), int(r_k))

    elif a < d and g:
        p_d = -(d // a)
        r_d = p_d * (a) + d
        r_e = p_d * (b) + e
        r_f = p_d * (c) + f

        p_g = -(g // a)
        r_g = p_g * (a) + g
        matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, h, k]]))

        p_re = -(h // r_e)
        r_h = p_re * (r_e) + h
        r_k = p_re * (r_f) + k

        matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, r_h, r_k]]))
        print('2:', int(a), int(r_e), int(r_k))
    
    elif a == d or a == g:
        if a == d:
            p_d = -(d / a)
            r_d = p_d * (a) + d
            r_e = p_d * (b) + e
            r_f = p_d * (c) + f
            if a < g:
                p_g = -(g // a)
                r_g = p_g * (a) + g
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, h, k]]))
                p_re = -(h // r_e)
                r_h = p_re * (r_e) + h
                r_k = p_re * (r_f) + k
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, r_h, r_k]]))
                print('3.1:', int(a), int(r_e), int(r_k))

            elif a > g:
                p_g = -(g / a)
                r_g = p_g * (a) + g
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, h, k]]))
                p_re = -(h / r_e)
                r_h = p_re * (r_e) + h
                r_k = p_re * (r_f) + k
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, r_h, r_k]]))
                print('3.2:', int(a), int(r_e), int(r_k))
            elif a == g:
                p_g = -(g / a)
                r_g = p_g * (a) + g
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, h, k]]))
                p_re = -(h / r_e)
                r_h = p_re * (r_e) + h
                r_k = p_re * (r_e) + k 
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, r_h, r_k]]))
                print('3.3:', int(a), int(r_e), int(r_k))
        elif a == g:
            p_g = -(g / a)
            r_g = p_g * (a) + g
            if a > d:
                p_d = -(d // a)
                r_d = p_d * (a) + d
                r_e = p_d * (b) + e
                r_f = p_d * (c) + f
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, h, k]]))
                p_re = -(h / r_e)
                r_h = p_re * (r_e) + h 
                r_k = p_re * (r_f) + k
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, r_h, r_k]]))
                print('3.4:', int(a), int(r_e), int(r_k))
            
            elif a < d:
                p_d = -(d // a)
                r_d = p_d * (a) + d
                r_e = p_d * (b) + e
                r_f = p_d * (c) + f
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, h, k]]))
                p_re = -(h // r_e)
                r_h = p_re * (r_e) + h
                r_k = p_re * (r_e) + k
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, r_h, r_k]]))
                print('3.5:', int(a), int(r_e), int(r_k))
            elif a == d:
                p_d = -(d // a)
                r_d = p_d * (a) + d
                r_e = p_d * (b) + e
                r_f = p_d * (c) + f
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, h, k]]))
                p_re = -(h / r_e)
                r_h = p_re * (r_e) + h
                r_k = p_re * (r_f) + k
                matrix = np.concatenate((matrix, [[a, b, c], [r_d, r_e, r_f], [r_g, r_h, r_k]]))
                print('3.6:', int(a), int(r_e), int(r_k))
           
elim(2, 1, 0, 0, 1, 2, 2, 2, 1) #output: 2, 1, -3
