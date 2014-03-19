str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyr'q ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
sentence = str.split(' ')
for word in sentence:
    w = ''
    for char in word:       
        if char.isalpha() and char not in 'yz' :
            w += chr(ord(char)+2)
        if char == 'y':
            w += 'a'
        if char == 'z':
            w += 'b'
    print w

