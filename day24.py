import numpy as np
# python_list = [1,2,3,4,5]
# numy_array_from_list2 = np.array(python_list, dtype=float)
# print(numy_array_from_list2) 

# two_dimensional_list = [[0,1,2], [3,4,5], [6,7,8]]
# numpy_two_dimensional_list = np.array(two_dimensional_list)
# print(type (numpy_two_dimensional_list))
# print(numpy_two_dimensional_list)

# nums = np.array([1, 2, 3, 4, 5])
# print(nums)
# print('shape of nums: ', nums.shape)
# numpy_two_dimensional_list = np.array([[0,1,2],[3,4,5],[6,7,8]])
# print(numpy_two_dimensional_list)
# print('shape of numpy_two_dimensional_list: ', numpy_two_dimensional_list.shape)
# three_by_four_array = np.array([[0, 1, 2, 3],[4,5,6,7],[8,9,10,11]])
# print(three_by_four_array)
# print('shape of three_by_four_array: ', three_by_four_array.shape)

# int_lists = [-3, -2, -1, 0, 1, 2,3]
# int_array = np.array(int_lists)
# float_array = np.array(int_lists, dtype=float)

# print(int_array)
# print(int_array.dtype)
# print(float_array)
# print(float_array.dtype)

# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_plus_original = numpy_array_from_list  + 10
# print(ten_plus_original)

# numpy_array_from_list = np.array([1, 2, 3, 4, 5])
# print('original array: ', numpy_array_from_list)
# ten_times_original = numpy_array_from_list // 10
# print(ten_times_original)

# two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
# print(type (two_dimension_array))
# print(two_dimension_array)
# print('Shape: ', two_dimension_array.shape)
# print('Size:', two_dimension_array.size)
# print('Data type:', two_dimension_array.dtype)

# two_dimension_array = np.array([[1,2,3],[4,5,6], [7,8,9]])
# first_two_rows_and_columns = two_dimension_array[0:2, 0:2]
# print(first_two_rows_and_columns)

normal_array= np.random.normal(79, 15, 80)

import matplotlib.pyplot as plt
import seaborn as sns
# sns.set()
# plt.hist(normal_array, color="grey", bins=50)


# np_normal_dis = np.random.normal(5, 0.5, 100)
# np_normal_dis
# two_dimension_array = np.array([(1,2,3),(4,5,6), (7,8,9)])
# print(type (two_dimension_array))
# print(two_dimension_array)
# print('Shape: ', two_dimension_array.shape)
# print('Size:', two_dimension_array.size)
# print('Data type:', two_dimension_array.dtype)
    
# ## min, max, mean, median, sd
# print('min: ', two_dimension_array.min())
# print('max: ', two_dimension_array.max())
# print('mean: ',two_dimension_array.mean())
# # print('median: ', two_dimension_array.median())
# print('sd: ', two_dimension_array.std())



from scipy import stats
np_normal_dis = np.random.normal(5, 0.5, 1000) # mean, standard deviation, number of samples
np_normal_dis
## min, max, mean, median, sd
print('min: ', np.min(np_normal_dis))
print('max: ', np.max(np_normal_dis))
print('mean: ', np.mean(np_normal_dis))
print('median: ', np.median(np_normal_dis))
print('mode: ', stats.mode(np_normal_dis))
print('sd: ', np.std(np_normal_dis))

plt.hist(np_normal_dis, color="red", bins=21)
plt.show()