#This example demonstrate shared data space by different processes (solution)

import multiprocessing 

def square_list(mylist, result, square_sum): 
	""" 
	function to square a given list 
	"""
	# append squares of mylist to result array 
	for idx, num in enumerate(mylist): 
		result[idx] = num * num 

	# square_sum value 
	square_sum.value = sum(result) 

	# print result Array 
	print("Result(in process p1): {}".format(result[:])) 

	# print square_sum Value 
	print("Sum of squares(in process p1): {}".format(square_sum.value)) 

if _name_ == "_main_": 
	# input list 
	mylist = [1,2,3,4] 

	# creating Array of int data type with space for 4 integers 
	result = multiprocessing.Array('i', 4) 

	# creating Value of int data type 
	square_sum = multiprocessing.Value('i') 

	# creating new process 
	p1 = multiprocessing.Process(target=square_list, args=(mylist, result, square_sum)) 

	# starting process 
	p1.start() 

	# wait until the process is finished 
	p1.join() 

	# print result array 
	print("Result(in main program): {}".format(result[:])) 

	# print square_sum Value 
	print("Sum of squares(in main program): {}".format(square_sum.value)) 


"""
	Shared memory : multiprocessing module provides Array and Value objects to share data between processes.
	Array: a ctypes array allocated from shared memory.
	Value: a ctypes object allocated from shared memory.
"""