address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

mulA = ord(ram[low + (high * 0x100)])

a = list(a)
mulB = ord(a[1]) + (ord(a[0]) * 0x100)

product = mulA * mulB

mulHex = list(str(hex(product)))
while len(mulHex) < 6:
    mulHex.insert(2, "0")
a[0] = chr(int("".join(mulHex[-4:-2]), 16))
a[1] = chr(int("".join(mulHex[-2:]), 16))
a = "".join(a)