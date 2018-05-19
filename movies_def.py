def print_lol(the_list):
	for each_item in the_list:
		if isinstance(each_item,list):
			print_lol(each_item)
		else:
			print each_item
movies = ["The Holy Grail","The LIfe of Brian","The Meaning of Life",["GC",["MP","GC","TG","EI","TJ",["haha",["i love leilei",["leilei i love you",["520 is coming",["if i tell her",["songhuo",["case so song"]]]]]]]]]]
print_lol(movies)
