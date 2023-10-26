#Write a NumPy program to create a structured array from given student name, height, class and their data types. Now sort by class, then height if class are equal.

import numpy as np

data_type = [('name', 'S15'), ('class', int), ('height', float)]
students_details = [('James', 5, 48.5), ('Nail', 6, 52.5),('Paul', 5, 42.10), ('Pit', 5, 40.11)]

students = np.array(students_details, dtype=data_type) 
print("Original array:")
print(students)
print("Sort by class, then height if class are equal:")
print(np.sort(students, order=['class', 'height']))


#floors and truncated values of numpy array
import numpy as np
x = np.array([-1.6, -1.5, -0.3, 0.1, 1.4, 1.8, 2.0]) 
print("Original array:")
print(x) 
print("Floor values of the above array elements:") 
print(np.floor(x)) 
print("Ceil values of the above array elements:") 
print(np.ceil(x)) 
print("Truncated values of the above array elements:") 
print(np.trunc(x))
