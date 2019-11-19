import itertools
import re

def process_dictionary_xx_yy_zz(circuit_name, output):
	dictionary = output[circuit_name]
	list_of_keys = list(dictionary.keys())
	# print(list_of_keys)
	num_qubits = len(list_of_keys[0])
	# print(num_qubits)
	# list of numbers to iterate on
	list_of_nums = list(range(num_qubits))
	output = []
	for i in itertools.combinations(list_of_nums, 2):
		# find two indices to fix
		first = i[0]
		second = i[1]
		# fix 00 and sum
		zz = []
		s1 = 0
		for j in list_of_keys:
			if j[first] == "0" and j[second] == "0":
				zz.append(j)
		for k in zz:
			s1 += dictionary[k]
		# fix 01 and sum 
		zo = []
		s2 = 0
		for j in list_of_keys:
			if j[first] == "0" and j[second] == "1":
				zo.append(j)
		for k in zo:
			s2 += dictionary[k]

		# fix 10 and sum
		oz = []
		s3 = 0
		for j in list_of_keys:
			if j[first] == "1" and j[second] == "0":
				oz.append(j)
		for k in oz:
			s3 += dictionary[k]

		# fix 11 and sum
		oo = []
		s4 = 0
		for j in list_of_keys:
			if j[first] == "1" and j[second] == "1":
				oo.append(j)
		for k in oo:
			s4 += dictionary[k]

		total = (s1 - s2 - s3 + s4)/1024
		# print(s1, s2, s3, s4)
		output.append(total)

	return output


def process_dictionary_ix_iy_iz(circuit_name, output):
	dictionary = output[circuit_name]
	list_of_keys = list(dictionary.keys())
	# print(list_of_keys)
	num_qubits = len(list_of_keys[0])
	# print(num_qubits)
	# list of numbers to iterate on
	list_of_nums = list(range(num_qubits))
	output = []
	for i in itertools.combinations(list_of_nums, 2):
		# find two indices to fix
		first = i[0]
		second = i[1]
		# fix 00 and sum
		zz = []
		s1 = 0
		for j in list_of_keys:
			if j[first] == "0" and j[second] == "0":
				zz.append(j)
		for k in zz:
			s1 += dictionary[k]
		# fix 01 and sum 
		zo = []
		s2 = 0
		for j in list_of_keys:
			if j[first] == "0" and j[second] == "1":
				zo.append(j)
		for k in zo:
			s2 += dictionary[k]

		# fix 10 and sum
		oz = []
		s3 = 0
		for j in list_of_keys:
			if j[first] == "1" and j[second] == "0":
				oz.append(j)
		for k in oz:
			s3 += dictionary[k]

		# fix 11 and sum
		oo = []
		s4 = 0
		for j in list_of_keys:
			if j[first] == "1" and j[second] == "1":
				oo.append(j)
		for k in oo:
			s4 += dictionary[k]

		total = (s4 + s2 - s3 - s1)/1024
		# print(s1, s2, s3, s4)
		output.append(total)

	return output
