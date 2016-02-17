def min(list):
    
	min = list[0]
	for elm in list[1:]:
	    if elm < min:
	        min = elm
	print ("The minimum value in the list is: " + str(min))

print (min([10,7,41,4]))