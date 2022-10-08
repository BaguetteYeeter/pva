address += 1
register = ord(ram[address])

regs = [a, a, b, c, d, e, f]
regstr = ["a", "a", "b", "c", "d", "e", "f"]

register = regs[register]

value = stack.pop()

valueHex = list(str(hex(value)))
while len(valueHex) < 6:
    valueHex.insert(2, "0")
register[0] = chr(int("".join(valueHex[-4:-2]), 16))
register[1] = chr(int("".join(valueHex[-2:]), 16))
register = "".join(register)

exec("%s = register" % regstr[ord(ram[address])])