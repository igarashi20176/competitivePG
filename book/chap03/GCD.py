def bubun(i, w, a):
    if i == 0 :
        return True if w == 0 else False
        
    if bubun( i-1, w, a ): 
        return True

    print(f'index: {i}, w: {w}')

    if bubun( i-1, w-a[i-1], a ):
        return True

    print(f'index: {i}, w: {w}')
    
    return False


int_ary = [ 2, 3, 4 ]

if bubun( len(int_ary), 6, int_ary ):
    print("success")
else:
    print("fault")