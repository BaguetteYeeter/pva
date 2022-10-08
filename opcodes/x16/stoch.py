address += 1
high = ord(ram[address])
address += 1
low = ord(ram[address])

movaddress = low + (high * 0x100)

ram = list(ram)
ram[movaddress] = c[0]
ram = "".join(ram)
