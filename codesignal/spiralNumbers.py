def spiralNumbers(n):
    
    matrix = list()
    
    for r in range(0, n):
        
        row = list()
        
        for _ in range(0, n):
            
            row.append(False)
            
        matrix.append(row)
            
            
    
    
    current = 1
    i = 0
    j = 0
         
    while current < n * n:
        
        
        while go_right(matrix, i, j, n):

            matrix[i][j] = current
            j += 1
            current += 1
            
        if matrix[i][j] == False:
            matrix[i][j] = current
            current += 1
        
        
        i += 1
        while go_bottom(matrix, i, j, n):
            
            matrix[i][j] = current
            i += 1
            current += 1
            
        if matrix[i][j] == False:
            matrix[i][j] = current
            current += 1
            
        
        j -= 1
       
        while go_left(matrix, i, j, n):
            
            matrix[i][j] = current
            j -= 1
            current += 1
        
        if matrix[i][j] == False:
            matrix[i][j] = current
            current += 1
        
            
        i -= 1
       
        while go_top(matrix, i, j, n):
            
            matrix[i][j] = current
            i -= 1 
            current += 1
            
         
        if matrix[i][j] == False:
            matrix[i][j] = current
            current += 1
        
        j += 1
        
    if matrix[i][j] == False:
            matrix[i][j] = current
                
    return matrix
            
            
        
    
    
def go_right(arr, i, j, n):
    
    if j + 1 < n and arr[i][j + 1] is False:

        return True
        
    return False
    
    
def go_bottom(arr, i, j, n):
    
    
    if i + 1 < n  and arr[i + 1][j] is False:
        
        return True
        
    return False
    
    
def go_left(arr, i, j, n):
    
    if j - 1 >= 0 and arr[i][j - 1] is False:
        
        return True
        
    return False


def go_top(arr, i, j, n):
    
    if i - 1 >= 0 and arr[i - 1][j] is False:
        
        return True
        
    return False
    
    

