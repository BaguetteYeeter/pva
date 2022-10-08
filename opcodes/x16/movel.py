address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

movaddress = low + (high * 0x100)

e = list(e)
e[1] = ram[movaddress]
e = "".join(e)