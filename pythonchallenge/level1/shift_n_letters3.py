text="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
result=""
for i in text:
    if (ord(i) >= ord('a') and ord(i) <= ord('z')):
            result += chr((ord(i)+2 - ord('a'))%26 + ord('a'))
    else:
            result += i
print result
