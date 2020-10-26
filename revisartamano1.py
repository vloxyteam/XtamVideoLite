# Python program to explain os.path.getsize() method 
    
# importing os module 
import os 

# Path 
path = './'

# Get the size (in bytes) 
# of specified path 
size1 = os.path.getsize(path) 


# Print the size (in bytes) 
# of specified path 
print("El tamaño en (bytes) of '%s':" %path, size1) 
