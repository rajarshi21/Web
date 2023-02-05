import numpy as np

# Print basic numpy array
# The below is called a ndarray
arr = np.array([1, 2, 3, 4, 5])
print(arr)

# Print numpy version
print('Print numpy version')
print(np.__version__)

# Array indexing - 1D
arr = np.array([1, 2, 3, 4])
print("1-D array indexing")
print(arr[0])  # 1st ele
print(arr[1])  # 2nd ele
# Array indexing - 2D
print("2-D array indexing")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('2nd element on 1st row: ', arr[0, 1])
# Array indexing - 3D
print("3-D array indexing")
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr[0, 1, 2])
# Negative indexing
print("Negative indexing")
arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print('Last element from 2nd dim: ', arr[1, -1])

# Data types in numpy
# Create an array with data type string
arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# Create an array with datatype 4 bytes integer
arr = np.array([1, 2, 3, 4], dtype='i4')
print(arr)
print(arr.dtype)

# Converting data type from float to integer
arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')  # use of astype
print(newarr)
print(newarr.dtype)

# Copy and view

# Copy
arr = np.array([1, 2, 3, 4, 5])
x = arr.copy()
arr[0] = 42  # Make changes in arr only
print("Copy")
print(arr)
print(x)

# View
arr = np.array([1, 2, 3, 4, 5])
x = arr.view()  # Make changes in both
arr[0] = 42
print("View")
print(arr)
print(x)

# To check if the array owns the data or not
arr = np.array([1, 2, 3, 4, 5])

x = arr.copy()  # Here x(copy) owns the data
y = arr.view()  # Here the y(view) do not own the data

print(x.base)
print(y.base)

# Shape of a 2-D array
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print("shape of 2D array")
print(arr.shape)

# Create an array with 5 dimensions using ndmin
arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('shape of array :', arr.shape)

# Reshaping arrays
# Reshape from 1-D to 2-D
print('1-D to 2-D')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(4, 3)
print(newarr)
# Reshape from 1-D to 3-D
print('1-D to 3-D')
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
newarr = arr.reshape(2, 3, 2)
print(newarr)

# Returns Copy or View? - TODO
# Unknown Dimension - TODO
# Flattening the arrays - TODO

# Array iteration - TODO
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# Numpy array join

print("Joining 1-D array")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)
# Joining 2-D arrays along rows
print("Joining 2-D array")
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)
# Joining arrays using stack function
print("Joining arrays using the stack function => axis=1 ")
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)
# Stacking along rows/columns
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
print("Stacking along rows")
arr = np.hstack((arr1, arr2))
print(arr)
print("Stacking along columns")
arr = np.vstack((arr1, arr2))
print(arr)
print("stacking along height")
arr = np.dstack((arr1, arr2))
print(arr)

# Splitting Numpy arrays
# Splitting 1-D array
arr = np.array([1, 2, 3, 4, 5, 6])
newarr = np.array_split(arr, 3)
print(newarr)
newarr = np.array_split(arr, 4)
print(newarr)
# You can also access the split arrays
print(newarr[0])
print(newarr[1])
print(newarr[2])
# Splitting 2-D array
print('Splitting 2-D array - 1')
arr = np.array([[1, 2], [3, 4], [5, 6], [7, 8], [9, 10], [11, 12]])
newarr = np.array_split(arr, 3)
print(newarr)
print('Splitting 2-D array - 2')
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3)
print(newarr)
# Split the 2-D array into three 2-D arrays along rows
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.array_split(arr, 3, axis=1)
print(newarr)
# Split the 2-D array into three 2-D arrays along rows using hsplit(opposite of hstack)
arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
newarr = np.hsplit(arr, 3)
print(newarr)

# Numpy array searching
# Find the indexes where the value is 4
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print("Printing the indices as a tuple, containing the indices and the datatype")
print(x)
# Find the indexes where the values are even
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])
print("indexes where the values are even")
x = np.where(arr % 2 == 0)
print(x)
print("indexes where the values are odd")
x = np.where(arr % 2 == 1)
print(x)

# NumPy Sorting Arrays
print('Numpy Sorting Arrays')
print('Sort the array numerically')
arr = np.array([3, 2, 0, 1])
print(np.sort(arr))
print('Sorting the array alphabetically')
arr = np.array(['banana', 'cherry', 'apple'])
print(np.sort(arr))
arr = np.array([True, False, True])
print('Sorting a boolean array')
print(np.sort(arr))
print('Sorting a 2-D array')
arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

# NumPy filter array
print("Filtering arrays")
# Create an array from the elements on index 0 and 2
arr = np.array([41, 42, 43, 44])
x = [True, False, True, False]
print("Filtering wherever the value is True")
newarr = arr[x]
print(newarr)
# Creating the filter array
# Create a filter array that will return only values higher than 42 - TODO
arr = np.array([41, 42, 43, 44])
filter_arr = []
for item in arr:
    if item > 42:
        filter_arr.append(True)
    else:
        filter_arr.append(False)

newarr = arr[filter_arr]
print(filter_arr)
print(newarr)
# Filter array to get the even elements
arr = np.array([1, 2, 3, 4, 5, 6, 7])
filter_arr = []
for item in arr:
    if item % 2 == 0:
        filter_arr.append(True)
    else:
        filter_arr.append(False)
# The lines 219~224 can be replaced as below:
#filter_arr = arr % 2 == 0
newarr = arr[filter_arr]
print("Even array is as below")
print(newarr)

