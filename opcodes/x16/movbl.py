address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

movaddress = low + (high * 0x100)

b = list(b)
b[1] = ram[movaddress]
b = "".join(b)
