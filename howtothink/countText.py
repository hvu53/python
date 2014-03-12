""" 
	Assign to a variable in your program a triple-quoted string that contains your favorite paragraph of text - perhaps a poem, a speech, instructions to bake a cake, some inspirational verses, etc.

	Write a function that counts the number of alphabetic characters (a thru z, or A thru Z) in your text and then keeps track of how many are the letter e. Your function should print an analysis of the text like this:
"""
import string
def countText(text,target):
	lower_alpha = string.ascii_lowercase
	upper_alpha = string.ascii_uppercase
	count = 0
	totalChar = 0
	for char in text:
		if char in lower_alpha or char in upper_alpha:
			totalChar +=1
			if char == target:
				count +=1

	percent_target = (float(count)/float(totalChar)) * 100
	print ("Your text contains", totalChar, "alphabetic characters of which", count, "(", percent_target,"%)", "are",target)

text = '''
	"If the automobile had followed the same development cycle as the computer, a
Rolls-Royce would today cost $100, get a million miles per gallon, and explode
once a year, killing everyone inside."
-Robert Cringely
'''
countText(text,"e")