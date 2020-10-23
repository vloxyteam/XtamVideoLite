# Python program to explain os.path.getsize() method 
    
# importing os module 
import os 

# Path 
path = '/home/xtam/camaras/camara1/'

# Get the size (in bytes) 
# of specified path 
size = os.path.getsize(path) 


# Print the size (in bytes) 
# of specified path 
print("Size (In bytes) of '%s':" %path, size) 
