address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

powA = ord(ram[low + (high * 0x100)])

a = list(a)
powB = ord(a[1]) + (ord(a[0]) * 0x100)

powers = powA ** powB

powHex = list(str(hex(powers)))
while len(powHex) < 6:
    powHex.insert(2, "0")
a[0] = chr(int("".join(powHex[-4:-2]), 16))
a[1] = chr(int("".join(powHex[-2:]), 16))
a = "".join(a)