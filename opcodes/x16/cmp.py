regA = ord(a[1]) + (ord(a[0]) * 0x100)
regB = ord(b[1]) + (ord(b[0]) * 0x100)

c = list(c)
c[1] = chr(0)

if regA == regB:
    c = [chr(0), chr(1)]
elif regA > regB:
    c = [chr(0), chr(2)]
elif regA < regB:
    c = [chr(0), chr(3)]
else:
    c = [chr(0), chr(0)]

c = "".join(c)