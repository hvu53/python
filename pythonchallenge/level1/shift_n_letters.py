def shift_n_letters(aStr, n):
    newStr = ''
    for i in aStr:
        if i in ' .()':
            newStr += i
        v = ord(i)
        if v +n > 122:
            new_v = 96 + (v+n -122)
        elif v+n < 97:
            new_v = 122 - (96 - (v+n))
        elif v+n >= 97 and v+n <= 122:
            new_v = v + n
        newStr += chr(new_v)
    return newStr

astr = """g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr
... amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q
 ... ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb.
... lmu ynnjw ml rfc spj."""
print shift_n_letters(astr,2)
