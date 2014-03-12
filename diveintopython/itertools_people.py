import itertools
names = list(open('examples/favorite-people.txt', encoding='utf-8'))
names = [name.rstrip() for name in names]
# sorted function can also take a function as the key parameter, & it sorts by that key
names = sorted(names,len)


# string manipulation translate
translation_table = {ord('A'): ord('O')}
'MARK'.translate(translation_table)