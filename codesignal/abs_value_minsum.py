def absoluteValuesSumMinimization(a):
    
    sum_dict = dict()
    
    for i in range(len(a)):
        
        if a[i] not in sum_dict:
            
            sum_dict[a[i]] = 0
            
        else:
            
            continue
        
        for j in range(len(a)):

            sum_dict[a[i]] += abs(a[i] - a[j])
            
        
    min_elem = None
    
    for k in sum_dict:
        
        
        if min_elem is None:
            
            min_elem = k
            continue
            
            
        if sum_dict[k] < sum_dict[min_elem]:
            
            min_elem = k
            
        
            
    return min_elem
            
                
        