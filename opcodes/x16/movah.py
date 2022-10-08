address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

movaddress = low + (high * 0x100)

a = list(a)
a[0] = ram[movaddress]
a = "".join(a)
