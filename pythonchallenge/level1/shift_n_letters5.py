# using dictionary

import string
cypher = dict(zip(string.lowercase, string.lowercase[2:]+ string.lowercase[:2]))
text = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.  lmu ynnjw ml rfc spj."

print cypher
print "".join(cypher.get(c,c) for c in text)
