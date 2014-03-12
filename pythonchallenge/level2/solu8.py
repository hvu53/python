import string
for c in text:
    if not ((c in string.punctuation) or (c=="\n")): print c
