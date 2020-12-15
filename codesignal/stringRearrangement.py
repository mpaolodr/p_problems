from itertools import permutations 

def stringsRearrangement(inputArray):
    
    perms = permutations(inputArray, len(inputArray))

    for p in perms:
        
        if helper(p) == True:
            
            return True
            
    return False
    

def helper(arr):
    
    
    for i in range(len(arr) - 1):
        
        word1 = arr[i]
        word2 = arr[i + 1]
       
        diff = 0
        
        for x,y in zip(word1, word2):
            
            if x != y:
                
                diff += 1
                
                
        if diff > 1 or diff == 0:
            
            return False
            
            
    return True
        