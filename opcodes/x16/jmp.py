address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

jmpaddress = low + (high * 0x100)

address = jmpaddress - 1
