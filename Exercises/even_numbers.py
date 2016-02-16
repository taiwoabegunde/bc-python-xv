def even_numbers(lower, higher):
	if lower > higher:
		print ("error: higher must be greater than lower") 
	else:
		for i in range(lower, higher+1):
			if i%2==0:
				print (i)
