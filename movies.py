movies = ["The Holy Grail","The LIfe of Brian","The Meaning of Life",["GC",["MP","GC","TG","EI","TJ"]]]
print movies
movies.insert(1,1975)
movies.insert(3,1979)
movies.append(1983)
print movies
for each_item in movies:
	if isinstance(each_item,list):
		for nested_item in each_item:
			if isinstance(nested_item,list):
				for third_item in nested_item:
					print third_item
			else:
				print nested_item
	else:
		print each_item

