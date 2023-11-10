def addition(n):
    n = n + 1 
    return n 
  
 
numbers = [1, 2, 3, 4] 
result = map(addition, numbers) 
print(list(result)) 
