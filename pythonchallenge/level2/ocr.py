import string
dict = {}
# with open('mess.txt', 'r') as f:
#     for line in f:
#         for i in list(line.strip()):
#             if i not in dict:
#                 dict[i] = 1
#             else:
#                 dict[i] +=1
# s = ''
# for k,v in dict.items():
#   if v ==1:
#     s += k
# print dict
# print s
s = ''
x = string.ascii_lowercase
with open('mess.txt', 'r') as f:
    for line in f:
      for char in list(line.strip()):
        if char in x:
          s += char

print s
