# U - A SET is a collection of unique items
# create a function that sorts through lists removes all dupe items from it
# return the new list
# assign the newly set list a variable
# in that variable, wrap lst parameter in set() function
# return variable


# P -
# new_list = set(lst)
# return new_list

# E - 
    # new_list = set(lst)
    # return new_list
list_a = [2,3,4,6,7,7,7,4,3,4,2,1,8]

def setify(lst):
	remove_dupes = set(lst)
	sorted_list = sorted(remove_dupes)
	return sorted_list

print('List A')
print(setify(list_a))

# R - 
# You can wrap methods in methods and return the value from that
# example:
print('List B')
list_b = [2,3,4,6,7,7,7,4,3,4,2,1,8,5,5]

def setify_2(lst):
	return (sorted(set(lst)))

print(setify_2(list_b))
