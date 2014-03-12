def mating_pairs(males, females):
	""" set, set -> set
	take 2 equal-sized sets
	returns a set of pairs, each pair is a tuple with 1 male, 1 female
	"""
	length = len(males)
	mates = set()
	for i in range(length):
		mates.add((males.pop(), females.pop()))

	return mates

print(mating_pairs({1,2,3,4},{5,6,7,8}))


def mating_pairs2(first, second):

""" (set, set) -> set of tuples
Return a set of tuples.
>>>mating_pairs({'Botta_m', 'Wagner_m', 'James_m', 'Somalian_m', 'Lowe_m'}, {'Botta_f', 'Wagner_f', 'James_f', 'Somalian_f', 'Lowe_f'})
{('Botta_m', 'Botta_f'), ('Wagner_m', 'Wagner_f'), ('James_m',  'James_f'), ('Lowe_m', 'Lowe_f'), ('Somalian_m', 'Somalian_f')}
"""
pair_list = set()
some_list = set()
males = first
females = second
list_len=len(males)
for i in range(list_len):
    male = males.pop()[0:-2]
    female = females.pop()[0:-2]
    if male == female:
        some_list.add((male, female))
    else:
        push_in = (male,' ' )
        some_list.add(push_in)
        push_in = (female,' ' )
        some_list.add(push_in)
        for entry in some_list:
            if entry[0]==' ':
                some_list.remove(entry)
                some_list.add((male, entry[1]))                    
            if entry[1]==' ':
                some_list.remove(entry)
                some_list.add((entry[0], female))
for pair in some_list:
    if pair[0]==pair[1]:
        pair_list.add((pair[0] + '_m', pair[1] + '_f'))
return pair_list