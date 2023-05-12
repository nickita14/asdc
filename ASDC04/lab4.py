import numpy as np
import time

class MultiDimensionalArray:
    def __init__(self, dimensions):
        # Initialize a numpy array with the specified dimensions, filled with random numbers.
        self.array = np.random.rand(*dimensions)
        
        # Store the dimensions and the total number of elements in the array.
        self.dimension_sizes = np.array(dimensions)
        self.dimension_sizes_sum = np.prod(self.dimension_sizes)

    def direct_access(self, indices):
        # Record the start time of the operation.
        start_time = time.perf_counter()
        
        # Use numpy's indexing to directly access the element at the specified indices.
        result = self.array[tuple(indices)]
        
        # Record the end time of the operation and print the elapsed time.
        end_time = time.perf_counter()
        print("Direct Access Time: ", end_time - start_time)
        
        return result

    def illiffe_vector_access(self, indices):
        start_time = time.perf_counter()
        
        # Iteratively index into the array using each index in the list of indices.
        result = self.array
        for idx in indices:
            result = result[idx]
            
        end_time = time.perf_counter()
        print("Illiffe Vector Access Time: ", end_time - start_time)
        
        return result

    def defining_vector_access(self, indices):
        start_time = time.perf_counter()
        
        # Calculate the offset in the flattened version of the array using the defining vector method.
        offset = 0
        len_indices = len(indices)
        for i in range(len_indices):
            offset += indices[i] * self.dimension_sizes[len_indices - i - 1]
        offset -= self.dimension_sizes_sum
        
        # Access the element at the calculated offset in the flattened array.
        result = self.array.flat[offset]  
        
        end_time = time.perf_counter()
        print("Defining Vector Access Time: ", end_time - start_time)
        
        return result

if __name__ == "__main__":
    # Create a 1000x1000x1000 multidimensional array.
    mda = MultiDimensionalArray((1000, 1000, 1000))
    
    # Access an element using each of the three methods and print the result.
    print(mda.direct_access((500, 500, 500)))
    print(mda.illiffe_vector_access([500, 500, 500]))  
    print(mda.defining_vector_access((500, 500, 500)))  
