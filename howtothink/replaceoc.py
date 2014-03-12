def rem(text, chr):
	for ch in text:
		if ch == chr:
			text = text.replace(ch,"")
	return text

print rem("hoa vu", "o")