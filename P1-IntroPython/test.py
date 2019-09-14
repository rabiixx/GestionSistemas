# Python3 List Methods


# append(): add a single element at the end of the list

	# animal list
	animal = ['cat', 'dog', 'rabbit']

	# an element is added
	animal.append('guinea pig')

	#Updated Animal List
	print('Updated animal list: ', animal)

	# >>>Updated animal list:  ['cat', 'dog', 'rabbit', 'guinea pig']


# extend(): Add Elements of a list to another list

# insert(index, type): Add a elements in the gives index

	mixed_list = [{1, 2}, [5, 6, 7]]

	# number tuple
	number_tuple = (3, 4)

	# inserting tuple to the list
	mixed_list.insert(1, number_tuple)

	print('Updated List: ', mixed_list)

	#################

	# vowel list
	vowel = ['a', 'e', 'i', 'u']

	# inserting element to list at 4th position
	vowel.insert(3, 'o')

	print('Updated List: ', vowel)


# remove(): Removes Element from the List

	# animal list
	animal = ['cat', 'dog', 'rabbit', 'guinea pig']

	# 'rabbit' element is removed
	animal.remove(animal[1])
	animal.remove('rabbit')

	#Updated Animal List
	print('Updated animal list: ', animal)


# index(element): returns smallest index if element in list

	# vowels list
	vowels = ['a', 'e', 'i', 'o', 'i', 'u']

	# element 'e' is searched
	index = vowels.index('e')

	# index of 'e' is printed
	print('The index of e:', index)

	# element 'i' is searched
	index = vowels.index('i')

	# only the first index of the element is printed
	print('The index of i:', index)

	# >>> The index of e: 1
	# >>> The index of i: 2

# count(element): returns occurrences of element in a list 

# pop(index): Removes element at given index

# sort(): sorts elements of a list

# clear(): removes all items from a list

# 

