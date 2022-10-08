address += 1
register = ord(ram[address])

regs = [a, a, b, c, d, e, f]

register = regs[register]

value = ord(register[1]) + (ord(register[0]) * 0x100)
stack.append(value)